NULL =

pkglibdir = $(KA_PLUGINS_DIR)

if ENABLE_PAM_PLUGIN
  PAM_PLUGIN = libka-plugin-pam.la
else
  PAM_PLUGIN =
endif

pkglib_LTLIBRARIES = \
	libka-plugin-dummy.la \
	$(PAM_PLUGIN) \
	$(NULL)

# Dummy example plugin
libka_plugin_dummy_la_SOURCES = \
	ka-plugin-dummy.c \
	ka-plugin-dummy.h \
	$(NULL)

libka_plugin_dummy_la_CPPFLAGS = \
	$(GTK_CFLAGS)       \
	-I$(top_srcdir)/src \
	$(NULL)

libka_plugin_dummy_la_LDFLAGS = \
	-module \
	-avoid-version \
	$(NULL)

# PAM plugin
if ENABLE_PAM_PLUGIN
libka_plugin_pam_la_SOURCES = \
	ka-plugin-pam.c \
	ka-plugin-pam.h \
	$(NULL)

libka_plugin_pam_la_CPPFLAGS = \
	$(GTK_CFLAGS)       \
	-I$(top_srcdir)/src \
	$(NULL)

libka_plugin_pam_la_LDFLAGS = \
	-module \
	-avoid-version \
	$(PAM_LIBS) \
	$(NULL)
endif