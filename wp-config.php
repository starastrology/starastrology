<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * Localized language
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'local' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', 'root' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',          'n)()P/N0]KeH(+9DN|)j]R]1ODk#T}Ut5gaSQw+#%Fur5&v[%2:}Me4Iq4%s>.&r' );
define( 'SECURE_AUTH_KEY',   'OAZCG0N<y<cqJ)Sms]#Qy3Ku(k_iXK(i4gyPLx<MK1K&:|L3`{T$v/|gbI=PpN|F' );
define( 'LOGGED_IN_KEY',     '|%@e)0WCepl!Vl[/Kx?EZXDym]FP&SB!nqczur2C!3qQ2g9MAg|SF-3y>(o{Bypr' );
define( 'NONCE_KEY',         '(mhLFG#bRPPEP<=)2$X7Y.N26TLPFz![F>Ic.6fuR<tCfmF}eIUWF##7$QDq73tn' );
define( 'AUTH_SALT',         '>riiFGw0sa!nXh.Us9>z;2lUd 9;3xtl0-(WG_!X,sR+?Pk|mSgsBj[(>H6/B]T9' );
define( 'SECURE_AUTH_SALT',  'j,|,0o;uz) /?nSp7!l+0f32m:1TfQI5n$N.&^@39D)U_JJ{~b9.RDYxOckzBrF|' );
define( 'LOGGED_IN_SALT',    'CqxooCHGKMN= ViUroId`hym2r2(i`i*4^NXxz-%WgxLLD6lE|!:Tzo<TS/)fbiV' );
define( 'NONCE_SALT',        'pp]tqu_C8^tVm.ztBQPU3,lE ~jhp9g<^r.B5A*]1r_E?0D5qE~*QOa!8!Di#C2N' );
define( 'WP_CACHE_KEY_SALT', 'FVM>5a>zPzo^!)bWpaYWhYJD{J,:sO^3k 28l.O0@+MP_}bhCa`hMm9dLB|%C14f' );


/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';


/* Add any custom values between this line and the "stop editing" line. */



/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
if ( ! defined( 'WP_DEBUG' ) ) {
	define( 'WP_DEBUG', false );
}

define( 'WP_ENVIRONMENT_TYPE', 'local' );
/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
