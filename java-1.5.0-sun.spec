%define	origin		sun
%define	priority	1503
%define	javaver		1.5.0
%define	cvsver		1_5_0
%define	over		5.0
%define	buildver	11

%define	cvsversion	%{cvsver}_%{buildver}

%define	javaws_ver	%{javaver}
%define	javaws_version	%{cvsversion}

%define	jdkbundle	jdk%{javaver}_%{buildver}
%define	sdklnk		java-%{javaver}-%{origin}
%define	jrelnk		jre-%{javaver}-%{origin}
%define	sdkdir		%{name}-%{version}
%define	jredir		%{sdkdir}/jre
%define	sdkbindir	%{_jvmdir}/%{sdklnk}/bin
%define	sdklibdir	%{_jvmdir}/%{sdklnk}/lib
%define	jrebindir	%{_jvmdir}/%{jrelnk}/bin
%define	jvmjardir	%{_jvmjardir}/%{name}-%{version}

%define fontdir		%{_datadir}/fonts/java

%ifarch %{ix86}
%define	target_cpu	i586
%define	pluginname	%{_jvmdir}/%{jredir}/plugin/i386/ns7/libjavaplugin_oji.so
%endif
%ifarch x86_64
%define	target_cpu	amd64
%endif

%define	cgibindir	%{_var}/www/cgi-bin

# Avoid RPM 4.2+'s internal dep generator, it may produce bogus
# Provides/Requires here.
%define _use_internal_dependency_generator 0

# This prevents aggressive stripping.
%define	debug_package %{nil}

Name:		java-%{javaver}-%{origin}
Version:	%{javaver}.%{buildver}
Release:	%mkrel 9
Summary:	Java Runtime Environment for %{name}
License:	Operating System Distributor License for Java (DLJ)
Group:		Development/Java
URL:		http://java.sun.com/j2se/%{javaver}
Source0:	http://download.java.net/dlj/binaries/jdk-%{cvsversion}-dlj-linux-i586.bin
Source1:	http://download.java.net/dlj/binaries/jdk-%{cvsversion}-dlj-linux-amd64.bin
Source3:	jdk-dlj-ubuntu-svn20070206.tar.bz2
Source4:	java-sun-menu.xdg
Source5:	java-sun-directory.xdg
Source6:	java.sh
Source7:	java.csh
Patch0:		jdk-1.5.0_10-fix-control-panel.patch
Provides:	jre-%{javaver}-%{origin} = %{version}-%{release}
Provides:	jre-%{origin} = %{version}-%{release} j2re = %{version}-%{release}
Provides:	jre-%{javaver} java-%{javaver} jre = %{javaver}
Provides:	java-%{origin} = %{version}-%{release}
Provides:	java = %{javaver}
Obsoletes:	j2re
Requires:	update-alternatives
Requires:	jpackage-utils >= 0:1.5.38
BuildArch:	i586 x86_64
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	jpackage-utils >= 0:1.5.38 sed desktop-file-utils
%ifnarch x86_64
Provides:	javaws = %{javaws_ver}
%endif
Provides:	jndi = %{version} jndi-ldap = %{version}
Provides:	jndi-cos = %{version} jndi-rmi = %{version}
Provides:	jndi-dns = %{version}
Provides:	jaas = %{version}
Provides:	jsse = %{version}
Provides:	jce = %{version}
Provides:	jdbc-stdext = 3.0 jdbc-stdext = %{version}
Provides:	java-sasl = %{version}
%ifnarch x86_64
Obsoletes:	javaws-menu
Provides:	javaws-menu
%endif
# DLJ license requires these to be part of the JRE
%ifnarch x86_64
Requires:	%{name}-plugin = %{version}-%{release}
%endif
Requires:	%{name}-alsa = %{version}-%{release}
Requires:	%{name}-jdbc = %{version}-%{release}
Requires:	%{name}-fonts = %{version}-%{release}

%description
This package contains the Java Runtime Environment for %{name}

%package	devel
Summary:	Java Development Kit for %{name}
Group:		Development/Java
Requires:	update-alternatives
Provides:	java-sdk-%{javaver}-%{origin} = %{version}-%{release}
Provides:	java-sdk-%{origin} = %{version}-%{release} j2sdk = %{version}-%{release}
Provides:	java-sdk-%{javaver} java-sdk = %{javaver} jdk = %{javaver}
Provides:	java-devel-%{origin} = %{version}-%{release}
Provides:       java-%{javaver}-devel java-devel = %{javaver}
Obsoletes:	j2sdk
Requires:       %{name} = %{version}-%{release}

%description	devel
The Java(tm) Development Kit (JDK(tm)) contains the software and tools that
developers need to compile, debug, and run applets and applications
written using the Java programming language.

%package	src
Summary:	Source files for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}

%description	src
This package contains source files for %{name}.

%package	demo
Summary:	Demonstration files for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
# Without this a requirement on libjava_crw_demo_g.so is added which
# is not in the main java package. libjava_crw_demo.so is but not "_g".
AutoReq:        0

%description	demo
This package contains demonstration files for %{name}.

%ifnarch x86_64
%package	plugin
Summary:	Browser plugin files for %{name}
Group:		Networking/WWW
Requires:	%{name} = %{version}-%{release}
Provides:	java-plugin = %{javaver} java-%{javaver}-plugin = %{version}
Conflicts:	java-%{javaver}-ibm-plugin java-%{javaver}-blackdown-plugin
Conflicts:	java-%{javaver}-bea-plugin
Obsoletes:	java-1.3.1-plugin java-1.4.0-plugin java-1.4.1-plugin java-1.4.2-plugin

%description	plugin
This package contains browser plugin files for %{name}.
Note!  This package supports browsers built with GCC 3.2 and later.
%endif

%package	fonts
Summary:	TrueType fonts for %{origin} JVMs
Group:		System/Fonts/True type
Requires:	%{name} = %{version}-%{release} freetype-tools
Requires:	mkfontdir
Provides:	java-fonts = %{javaver} java-%{javaver}-fonts
Conflicts:	java-%{javaver}-ibm-fonts java-%{javaver}-blackdown-fonts
Conflicts:	java-%{javaver}-bea-fonts
Obsoletes:	java-1.3.1-fonts java-1.4.0-fonts java-1.4.1-fonts java-1.4.2-fonts

%description	fonts
This package contains the TrueType fonts for %{origin} JVMs.

%package	alsa
Summary:	ALSA support for %{name}
Group:		Development/Java
Requires:       %{name} = %{version}-%{release}

%description	alsa
This package contains Advanced Linux Sound Architecture (ALSA) support
libraries for %{name}.

%package	jdbc
Summary:	JDBC/ODBC bridge driver for %{name}
Group:		Development/Java
Requires:       %{name} = %{version}-%{release}
AutoReq:	0

%description	jdbc
This package contains the JDBC/ODBC bridge driver for %{name}.

%prep
%setup -q -T -c -n %{name}-%{version} -a3
%ifarch i586
sh %{SOURCE0} --accept-license --unpack
%else
sh %{SOURCE1} --accept-license --unpack
%endif
cd %{jdkbundle}
%ifnarch x86_64
%patch0 -p1
%else
rm -f man/man1/javaws.1
%endif

# fix perms
chmod -R go=u-w *
chmod -R u+w *

%build
for xdgmenu in debian/*desktop.in; do
	sed $xdgmenu \
	-e "s#@vendor@#Sun#g" \
	-e "s#@RELEASE@#%{javaver}#g" \
	-e "s#/@basedir@/bin#%{jrebindir}#g" \
	-e "s#Icon=.*#Icon=%{name}.png#g" \
	-e "s#@ia32txt@##g" \
	> %{name}-`echo $xdgmenu|cut -d- -f2|cut -d. -f1-2`
done
mv %{name}-java.desktop debian/sharedmimeinfo %{jdkbundle}/jre/lib

%ifnarch x86_64
sed %{SOURCE4} -e "s#@NAME@#%{name}#g" -e "s#@VERSION@#%{over}#g" > mandriva-%{name}.menu
sed %{SOURCE5} -e "s#@NAME@#%{name}#g" -e "s#@VERSION@#%{over}#g" > mandriva-%{name}.directory

sed -i -e "s#PATH=/usr/local/java/bin#PATH=%{jrebindir}#" %{jdkbundle}/bin/java-rmi.cgi

# fix up (create new) HtmlConverter
cat >%{jdkbundle}/bin/HtmlConverter << EOF
%{jrebindir}/java -jar %{sdklibdir}/htmlconverter.jar $*
EOF
%endif

%install
rm -rf %{buildroot}

cd %{jdkbundle}
%ifnarch x86_64
# install java-rmi-cgi
install -m755 bin/java-rmi.cgi -D %{buildroot}%{cgibindir}/java-rmi-%{version}.cgi
%endif

# main files
install -d %{buildroot}%{_jvmdir}/%{sdkdir}
cp -a  COPYRIGHT LICENSE THIRDPARTYLICENSEREADME.txt bin include lib %{buildroot}%{_jvmdir}/%{sdkdir}
install -m644 src.zip -D %{buildroot}%{_prefix}/src/%{name}-%{version}.zip
ln -s %{_prefix}/src/%{name}-%{version}.zip %{buildroot}%{_jvmdir}/%{sdkdir}/src.zip

install -d %{buildroot}%{_jvmdir}/%{jredir}

# extensions handling
install -d %{buildroot}%{jvmjardir}
pushd %{buildroot}%{jvmjardir}
   ln -s %{_jvmdir}/%{jredir}/lib/jsse.jar jsse-%{version}.jar
   ln -s %{_jvmdir}/%{jredir}/lib/jce.jar jce-%{version}.jar
   for jar in jndi jndi-ldap jndi-cos jndi-rmi jaas jdbc-stdext sasl; do
   ln -s %{_jvmdir}/%{jredir}/lib/rt.jar $jar-%{version}.jar; done
   ln -s jdbc-stdext-%{version}.jar jdbc-stdext-3.0.jar
   for jar in *-%{version}.jar ; do
      if [ x%{version} != x%{javaver} ]; then
         ln -fs ${jar} $(echo $jar | sed "s|-%{version}.|-%{javaver}.|g")
      fi
      ln -fs ${jar} $(echo $jar | sed "s|-%{version}.|.|g")
   done
popd

# rest of the jre
cp -a jre/bin jre/lib %{buildroot}%{_jvmdir}/%{jredir}
%ifnarch x86_64
cp -a jre/javaws jre/plugin %{buildroot}%{_jvmdir}/%{jredir}
%endif
install -d %{buildroot}%{_jvmdir}/%{jredir}/lib/endorsed

# jce policy file handling
install -d %{buildroot}%{_jvmprivdir}/%{name}/jce/vanilla
for file in local_policy.jar US_export_policy.jar; do
  ln -s %{_jvmdir}/%{jredir}/lib/security/$file \
    %{buildroot}%{_jvmprivdir}/%{name}/jce/vanilla
  # for ghosts
  touch %{buildroot}%{_jvmdir}/%{jredir}/lib/security/$file
done

# versionless symlinks
pushd %{buildroot}%{_jvmdir}
ln -s %{jredir} %{jrelnk}
ln -s %{sdkdir} %{sdklnk}
popd

pushd %{buildroot}%{_jvmjardir}
ln -s %{sdkdir} %{jrelnk}
ln -s %{sdkdir} %{sdklnk}
popd

%ifnarch x86_64

install -m644 jre/plugin/desktop/sun_java.png -D %{buildroot}%{_datadir}/pixmaps/%{name}.png

install -m644 ../mandriva-%{name}.menu -D %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged/mandriva-%{name}.menu
install -m644 ../mandriva-%{name}.directory -D %{buildroot}%{_datadir}/desktop-directories/mandriva-%{name}.directory

for desktop in ../*.desktop; do
	desktop-file-install	--vendor="" \
                        	--remove-category="Application" \
				--remove-category="X-Red-Hat-Base" \
				--remove-category="AdvancedSettings" \
				--add-category="X-MandrivaLinux-System-SunJava%{over}" \
                        	--dir %{buildroot}%{_datadir}/applications $desktop
done
%endif

# make sure that this directory exist so update-alternatvies won't fail if shared-mime-info isn't installed
install -d %{buildroot}%{_datadir}/mime/packages

# man pages
install -d %{buildroot}%{_mandir}/man1
pushd man
for manpage in man1/*; do
	iconv -f iso-8859-1 -t utf-8 $manpage -o %{buildroot}%{_mandir}/man1/`basename $manpage .1`-%{name}.1
	install -m644 ja_JP.eucJP/$manpage -D %{buildroot}%{_mandir}/ja_JP.eucJP/man1/`basename $manpage .1`-%{name}.1
done
popd

# demo
install -d %{buildroot}%{_datadir}/%{name}
cp -a demo %{buildroot}%{_datadir}/%{name}
ln -s %{_datadir}/%{name}/demo %{buildroot}%{_jvmdir}

### font handling
install -d %{buildroot}%{fontdir}
#mv %{buildroot}%{_jvmdir}/%{jredir}/lib/fonts %{buildroot}%{fontdir}
#ln -s %{fontdir} %{buildroot}%{_jvmdir}/%{jredir}/lib/fonts
ln -s %{_sysconfdir}/java/font.properties %{buildroot}%{_jvmdir}/%{jredir}/lib

# These %ghost'd files are created properly in %post  -- Rex
touch %{buildroot}%{fontdir}/{fonts.{alias,dir,scale,cache-1},XftCache,encodings.dir}

# fontpath.d symlink
mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%{fontdir} \
    %{buildroot}%_sysconfdir/X11/fontpath.d/java:pri=50

# make sure that plugin dir exists so update-alternatives won't fail if mozilla/firefox isn't installed
install -d %{buildroot}%{_libdir}/mozilla/plugins

cd ..

sed %{SOURCE6} -e "s#@JVM@#%{_jvmdir}/%{jredir}#g" | grep -v JDK_HOME > %{buildroot}%{_jvmdir}/%{jredir}/lib/java.sh
sed %{SOURCE7} -e "s#@JVM@#%{_jvmdir}/%{jredir}#g" | grep -v JDK_HOME > %{buildroot}%{_jvmdir}/%{jredir}/lib/java.csh
sed %{SOURCE6} -e "s#@JVM@#%{_jvmdir}/%{sdkdir}#g" > %{buildroot}%{_jvmdir}/%{sdkdir}/lib/java.sh
sed %{SOURCE7} -e "s#@JVM@#%{_jvmdir}/%{sdkdir}#g" > %{buildroot}%{_jvmdir}/%{sdkdir}/lib/java.csh
chmod 755 %{buildroot}%{_jvmdir}/%{jredir}/lib/java.*sh %{buildroot}%{_jvmdir}/%{sdkdir}/lib/java.*sh

# Most of this shamelessly stolen from redhat's kdebase-2.2.2 specfile
find %{buildroot}%{_jvmdir}/%{jredir} -type d \
| sed 's|'%{buildroot}'|%dir |' >  %{name}-%{version}-all.files
find %{buildroot}%{_jvmdir}/%{jredir} -type f -o -type l \
| sed 's|'%{buildroot}'||'      >> %{name}-%{version}-all.files

%ifnarch x86_64
grep plugin  %{name}-%{version}-all.files | sort \
> %{name}-%{version}-plugin.files
%endif
grep Jdbc    %{name}-%{version}-all.files | sort \
> %{name}-%{version}-jdbc.files
grep -F alsa.so %{name}-%{version}-all.files | sort \
> %{name}-%{version}-alsa.files
cat %{name}-%{version}-all.files \
| grep -v plugin \
| grep -v Jdbc \
| grep -v lib/fonts \
| grep -vF alsa.so \
| grep -v jre/lib/security \
> %{name}-%{version}.files

%ifarch x86_64
%define	jreext	%{nil}
%else
%define	jreext	javaws
%endif
%define	jrebin	keytool orbd policytool rmid rmiregistry servertool tnameserv
%define	jreman	java %{jreext} %{jrebin} kinit klist ktab
%ifarch	x86_64
%define	jdkext	%{nil}
%else
%define	jdkext	HtmlConverter
%endif
%define	jdkboth	appletviewer extcheck idlj jar jarsigner javadoc javah javap jdb native2ascii rmic serialver jconsole pack200 unpack200 apt jinfo jmap jps jsadebugd jstack jstat jstatd
%define	jdkman	%{jdkboth} javac
%define	jdkbin	%{jdkboth} %{jdkext}

for man in %{jreman}; do
echo %{_mandir}/man1/${man}-%{name}.1%{_extension} >> %{name}-%{version}.files
echo %{_mandir}/ja_JP.eucJP/man1/${man}-%{name}.1%{_extension} >> %{name}-%{version}.files
done
rm -f %{name}-%{version}-devel.files
for man in %{jdkman}; do
echo %{_mandir}/man1/${man}-%{name}.1%{_extension} >> %{name}-%{version}-devel.files
echo %{_mandir}/ja_JP.eucJP/man1/${man}-%{name}.1%{_extension} >> %{name}-%{version}-devel.files
done

%clean
rm -rf %{buildroot}

%post
update-alternatives --install %{_bindir}/java java %{jrebindir}/java %{priority}%{expand:%(for bin in %{jrebin}; do echo -n -e \ \\\\\\n\
--slave %{_bindir}/${bin}			${bin}			%{sdkbindir}/${bin}; done)}%{expand:%(for man in %{jreman}; do echo -n -e \ \\\\\\n\
--slave %{_mandir}/man1/${man}.1%{_extension}	${man}.1%{_extension}	%{_mandir}/man1/${man}-%{name}.1%{_extension}; done)}%{expand:%(for man in %{jreman}; do echo -n -e \ \\\\\\n\
--slave %{_mandir}/ja_JP.eucJP/man1/${man}.1%{_extension}	${man}%{_extension}.ja_JP.eucJP	%{_mandir}/ja_JP.eucJP/man1/${man}-%{name}.1%{_extension}; done)} \
%ifnarch x86_64
--slave %{_bindir}/ControlPanel			ControlPanel		%{jrebindir}/ControlPanel \
--slave %{_datadir}/javaws			javaws			%{jrebindir}/javaws \
%endif
--slave %{_datadir}/mime/packages/java.xml	java.xml		%{_jvmdir}/%{jrelnk}/lib/sharedmimeinfo \
--slave	%{_jvmdir}/jre				jre			%{_jvmdir}/%{jrelnk} \
--slave	%{_jvmjardir}/jre			jre_exports		%{_jvmjardir}/%{jrelnk} \
--slave %{_sysconfdir}/profile.d/java_20jre.sh	java_20jre.sh		%{_jvmdir}/%{jredir}/lib/java.sh \
--slave %{_sysconfdir}/profile.d/java_20jre.csh	java_20jre.csh		%{_jvmdir}/%{jredir}/lib/java.csh
# jre file with environment variables with has filename with higher number value than sdk to ensure
# sdk gets processed first

update-alternatives \
--install \
	%{_jvmdir}/%{jrelnk}/lib/security/local_policy.jar \
	jce_%{javaver}_%{origin}_local_policy \
	%{_jvmprivdir}/%{name}/jce/vanilla/local_policy.jar \
	%{priority} \
--slave \
	%{_jvmdir}/%{jrelnk}/lib/security/US_export_policy.jar \
	jce_%{javaver}_%{origin}_us_export_policy \
	%{_jvmprivdir}/%{name}/jce/vanilla/US_export_policy.jar

%ifnarch x86_64
%{update_desktop_database}
%endif
%{update_mime_database}

%post devel
update-alternatives --install %{_bindir}/javac javac %{sdkbindir}/javac %{priority}%{expand:%(for bin in %{jdkbin}; do echo -n -e \ \\\\\\n\
--slave %{_bindir}/${bin}			${bin}			%{sdkbindir}/${bin}; done)}%{expand:%(for man in %{jdkman}; do echo -n -e \ \\\\\\n\
--slave %{_mandir}/man1/${man}.1%{_extension}	${man}.1%{_extension}	%{_mandir}/man1/${man}-%{name}.1%{_extension}; done)}%{expand:%(for man in %{jdkman}; do echo -n -e \ \\\\\\n\
--slave %{_mandir}/ja_JP.eucJP/man1/${man}.1%{_extension}	${man}%{_extension}.ja_JP.eucJP	%{_mandir}/ja_JP.eucJP/man1/${man}-%{name}.1%{_extension}; done)} \
--slave	%{_jvmdir}/java				java_sdk		%{_jvmdir}/%{sdklnk} \
--slave	%{_jvmjardir}/java			java_sdk_exports	%{_jvmjardir}/%{sdklnk} \
--slave %{_sysconfdir}/profile.d/java_10sdk.sh	java_10sdk.sh		%{_jvmdir}/%{sdkdir}/lib/java.sh \
--slave %{_sysconfdir}/profile.d/java_10sdk.csh	java_10sdk.csh		%{_jvmdir}/%{sdkdir}/lib/java.csh

update-alternatives --install %{_jvmdir}/java-%{origin} java_sdk_%{origin} %{_jvmdir}/%{sdklnk} %{priority} \
--slave %{_jvmjardir}/java-%{origin}	java_sdk_%{origin}_exports	%{_jvmjardir}/%{sdklnk}

update-alternatives --install %{_jvmdir}/java-%{javaver} java_sdk_%{javaver} %{_jvmdir}/%{sdklnk} %{priority} \
--slave %{_jvmjardir}/java-%{javaver}	java_sdk_%{javaver}_exports      %{_jvmjardir}/%{sdklnk}

%ifnarch x86_64
%post plugin
update-alternatives --install %{_libdir}/mozilla/plugins/libjavaplugin_oji.so libjavaplugin_oji.so %{pluginname} %{priority}

%postun plugin
if [ "$1" = "0" ]; then
update-alternatives --remove libjavaplugin_oji.so %{pluginname}
fi
%endif

%postun
if [ "$1" = "0" ]; then
update-alternatives --remove java %{jrebindir}/java
update-alternatives --remove \
	jce_%{javaver}_%{origin}_local_policy \
	%{_jvmprivdir}/%{name}/jce/vanilla/local_policy.jar
update-alternatives --remove jre_%{origin}  %{_jvmdir}/%{jrelnk}
update-alternatives --remove jre_%{javaver} %{_jvmdir}/%{jrelnk}
fi
%ifnarch x86_64
%{clean_desktop_database}
%endif
%{clean_mime_database}

%postun devel
if [ "$1" = "0" ]; then
update-alternatives --remove javac %{sdkbindir}/javac
update-alternatives --remove java_sdk_%{origin}  %{_jvmdir}/%{sdklnk}
update-alternatives --remove java_sdk_%{javaver} %{_jvmdir}/%{sdklnk}
fi

%post fonts
%define	fonts	LucidaBrightItalic.ttf LucidaSansDemiBold.ttf LucidaTypewriterBold.ttf LucidaBrightDemiItalic.ttf LucidaBrightRegular.ttf LucidaSansRegular.ttf LucidaTypewriterRegular.ttf

update-alternatives --install %{fontdir}/LucidaBrightDemiBold.ttf LucidaBrightDemiBold.ttf  %{_jvmdir}/%{jredir}/lib/fonts/LucidaBrightDemiBold.ttf %{priority} \
%{expand:%(for font in %{fonts}; do echo -n -e \ \\\\\\n\
--slave %{fontdir}/$font	$font	%{_jvmdir}/%{jredir}/lib/fonts/$font; done)}

mkfontscale %{fontdir}
mkfontdir %{fontdir}

%postun fonts
if [ "$1" = "0" ]; then
update-alternatives --remove LucidaBrightDemiBold.ttf %{_jvmdir}/%{jredir}/lib/fonts/LucidaBrightDemiBold.ttf
fi

if [ -d %{fontdir} ]; then
mkfontscale %{fontdir}
mkfontdir %{fontdir}
fi

%files -f %{name}-%{version}.files
%defattr(-,root,root,-)
%doc %{jdkbundle}/jre/{CHANGES,COPYRIGHT,LICENSE,README}
%doc %{jdkbundle}/jre/Welcome.html
%dir %{_jvmdir}/%{sdkdir}
%{_jvmdir}/%{sdkdir}/COPYRIGHT
%{_jvmdir}/%{sdkdir}/LICENSE
%{_jvmdir}/%{sdkdir}/THIRDPARTYLICENSEREADME.txt
%{jvmjardir}
%{_jvmdir}/%{jredir}/lib/fonts
%dir %{_jvmdir}/%{jredir}/lib/security
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/cacerts
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.policy
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.security
%ifnarch x86_64
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/javaws.policy
%endif
%{_jvmdir}/%{jredir}/lib/security/local_policy.jar
%{_jvmdir}/%{jredir}/lib/security/US_export_policy.jar
%{_jvmdir}/%{jrelnk}
%{_jvmjardir}/%{jrelnk}
%{_jvmprivdir}/*
%ifnarch x86_64
%{_datadir}/applications/*.desktop
%{_sysconfdir}/xdg/menus/applications-merged/mandriva-%{name}.menu
%{_datadir}/desktop-directories/mandriva-%{name}.directory
%{_datadir}/pixmaps/*.png
%endif
%dir %{_datadir}/mime
%dir %{_datadir}/mime/packages

%files devel -f %{name}-%{version}-devel.files
%defattr(-,root,root,-)
%doc %{jdkbundle}/{COPYRIGHT,LICENSE,README.html}
%dir %{_jvmdir}/%{sdkdir}/bin
%dir %{_jvmdir}/%{sdkdir}/include
%dir %{_jvmdir}/%{sdkdir}/lib
%{_jvmdir}/%{sdkdir}/bin/*
%{_jvmdir}/%{sdkdir}/include/*
%{_jvmdir}/%{sdkdir}/lib/*
%{_jvmdir}/%{sdklnk}
%{_jvmjardir}/%{sdklnk}
%ifnarch x86_64
%{cgibindir}/java-rmi-%{version}.cgi
%endif

%files src
%defattr(-,root,root,-)
%{_jvmdir}/%{sdkdir}/src.zip
%{_prefix}/src/%{name}-%{version}.zip

%files demo
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/demo
%{_jvmdir}/demo

%files alsa -f %{name}-%{version}-alsa.files
%defattr(-,root,root,-)

%files jdbc -f %{name}-%{version}-jdbc.files
%defattr(-,root,root,-)

%ifnarch x86_64
%files plugin -f %{name}-%{version}-plugin.files
%defattr(-,root,root,-)
%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/plugins
%endif

%files fonts
%defattr(0644,root,root,0755)
%{_jvmdir}/%{jredir}/lib/fonts/*.ttf
%dir %{fontdir}
%config(noreplace) %{fontdir}/fonts.alias
%ghost %{fontdir}/fonts.dir
%ghost %{fontdir}/fonts.scale
%ghost %{fontdir}/fonts.cache-1
%ghost %{fontdir}/XftCache
%ghost %{fontdir}/encodings.dir
%{_sysconfdir}/X11/fontpath.d/java:pri=50


