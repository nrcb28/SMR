#!/usr/bin/env python3
"""Ejemplo didáctico SQLite: integridad, LEFT JOIN y rollback sin crear archivos."""

import json
import sqlite3


def demostrar() -> dict:
    db = sqlite3.connect(':memory:')
    try:
        db.execute('PRAGMA foreign_keys = ON')
        db.executescript('''
            CREATE TABLE equipo (
                id INTEGER PRIMARY KEY,
                codigo TEXT NOT NULL UNIQUE
            );
            CREATE TABLE incidencia (
                id INTEGER PRIMARY KEY,
                equipo_id INTEGER NOT NULL REFERENCES equipo(id),
                estado TEXT NOT NULL CHECK (estado IN ('abierta', 'cerrada'))
            );
            INSERT INTO equipo VALUES (1, 'PC-001'), (2, 'PC-002'), (3, 'PC-003');
            INSERT INTO incidencia VALUES (1, 1, 'abierta'), (2, 1, 'cerrada');
        ''')
        casos = [
            ('codigo_duplicado', 'INSERT INTO equipo VALUES (?, ?)', (4, 'PC-001')),
            ('referencia_inexistente', 'INSERT INTO incidencia VALUES (?, ?, ?)', (3, 999, 'abierta')),
            ('estado_invalido', 'INSERT INTO incidencia VALUES (?, ?, ?)', (3, 1, 'desconocido')),
        ]
        rechazos = []
        for nombre, sentencia, parametros in casos:
            try:
                with db:
                    db.execute(sentencia, parametros)
            except sqlite3.IntegrityError:
                rechazos.append(nombre)
            else:
                raise RuntimeError('Se esperaba rechazo de integridad: ' + nombre)
        antes = db.execute('SELECT estado FROM incidencia WHERE id = ?', (1,)).fetchone()[0]
        db.execute('BEGIN')
        db.execute('UPDATE incidencia SET estado = ? WHERE id = ?', ('cerrada', 1))
        db.rollback()
        despues = db.execute('SELECT estado FROM incidencia WHERE id = ?', (1,)).fetchone()[0]
        recuentos = db.execute('''
            SELECT e.codigo, COUNT(i.id)
            FROM equipo AS e
            LEFT JOIN incidencia AS i ON i.equipo_id = e.id
            GROUP BY e.id, e.codigo
            ORDER BY e.codigo
        ''').fetchall()
        if recuentos != [('PC-001', 2), ('PC-002', 0), ('PC-003', 0)] or antes != despues:
            raise RuntimeError('Resultado distinto del contrato didáctico')
        return {'recuentos': recuentos, 'rechazos_previstos': rechazos,
                'estado_antes': antes, 'estado_despues_de_rollback': despues,
                'nota': 'Datos sintéticos en memoria; no se han creado archivos de base de datos.'}
    finally:
        db.close()


if __name__ == '__main__':
    print(json.dumps(demostrar(), ensure_ascii=False, indent=2))
