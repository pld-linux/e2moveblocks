Summary:	e2moveblocks - tool to change layout of files on ext2/3 filesystems
Name:		e2moveblocks
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://lichota.net/~krzysiek/projects/e2moveblocks/%{name}-%{version}.tgz
# Source0-md5:	ea8e685247458b174c5f33085129812f
URL:		http://lichota.net/~krzysiek/projects/e2moveblocks/
BuildRequires:	e2fsprogs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
e2moveblocks is a tool which allows offline changing position of files
on ext2/ext3 filesystems. It can be used for defragging or grouping
files for prefetching.

WARNING: this tool is currently experimental and can destroy your
data. Use at your own risk, author is not responsible for any damages.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cxx}" \
	CFLAGS="%{rpmcxxflags}" \
	LDFLAGS="-lext2fs"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install e2blockmap ext3_optimize $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/e2blockmap
%attr(755,root,root) %{_sbindir}/ext3_optimize
