from .base import Centos_7


class Dotnet( Centos_7 ):
    scripts = (
        'ssh/provision.py',
        'dotnet/install.sh',
        'dotnet/post_install.sh',
        (
            'git_clone.py',
            'git@github.com:AptudeSiGRHA/clients_service.git',
            'main' ),
        (
            'git_clone.py',
            'git@github.com:AptudeSiGRHA/opportunities_service.git',
            'main' ),
        (
            'git_clone.py',
            'git@github.com:AptudeSiGRHA/ADLoginService.git',
            'main' ),
        (
            'dotnet/database_migration.sh',
            '/home/chibi/projects/clients_service__main/API_Clients/' ),
        ( "systemd/cp.py", 'dotnet/sigrha_clients.service' ),
        ( "systemd/systemd.py", 'enable', 'sigrha_clients.service' ),
        ( "systemd/systemd.py",'start', 'sigrha_clients.service' ),
    )


class Mitsuha( Dotnet ):
    pass