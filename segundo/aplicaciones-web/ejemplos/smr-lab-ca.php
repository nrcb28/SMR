<?php
/**
 * Plugin Name: SMR LAB - confianza HTTPS interna
 * Description: Selecciona el almacén CA Debian sólo para wp.aula.test en entorno local.
 * Version: 1.0.0
 *
 * Ejemplo educativo. Instalar como mu-plugin propiedad de root, no en uploads.
 * Requiere la CA pública LAB en el almacén Debian; nunca desactiva TLS.
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Ajusta únicamente las peticiones HTTPS canónicas del clon LAB.
 *
 * @param array  $args Argumentos de la HTTP API.
 * @param string $url  URL solicitada.
 * @return array
 */
function smr_lab_confianza_https_interna( $args, $url ) {
    if ( ! defined( 'WP_ENVIRONMENT_TYPE' ) || 'local' !== WP_ENVIRONMENT_TYPE ) {
        return $args;
    }

    $partes = wp_parse_url( $url );
    if ( ! is_array( $partes ) || empty( $partes['scheme'] ) || empty( $partes['host'] ) ) {
        return $args;
    }

    if ( 'https' !== strtolower( $partes['scheme'] )
        || 'wp.aula.test' !== strtolower( $partes['host'] )
        || ( isset( $partes['port'] ) && 443 !== (int) $partes['port'] ) ) {
        return $args;
    }

    $args['sslverify']       = true;
    $args['sslcertificates'] = '/etc/ssl/certs/ca-certificates.crt';
    // No trasladar los argumentos a otros destinos mediante redirecciones.
    $args['redirection'] = 0;

    return $args;
}

add_filter( 'http_request_args', 'smr_lab_confianza_https_interna', 10, 2 );
