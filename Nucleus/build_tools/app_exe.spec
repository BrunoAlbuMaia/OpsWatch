# build_tools/app_exe.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import os

# Defina o caminho absoluto para o diretório raiz do projeto
project_root = 'C:/Users/bruno.maia/source/repos/gitlab/fbbix/apicentralizador'  # Ajuste conforme necessário

# Adiciona todos os módulos do projeto
pathex = [
    project_root,
    os.path.join(project_root, 'Application'),
    os.path.join(project_root, 'Domain'),
    os.path.join(project_root, 'Infrastruncture'),
    os.path.join(project_root, 'Service'),
]

hiddenimports = [
    'Application',
    'Domain',
    'Infrastruncture',
    'Service',
]

datas = [
    (os.path.join(project_root, '.env'), '.')
]

a = Analysis(
    [os.path.join(project_root, 'app.py')],  # Atualizado para refletir o novo ponto de entrada
    pathex=pathex,  # Certifique-se de que o diretório raiz está no path
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,  # Inclua os módulos específicos aqui
    hookspath=[os.path.join(project_root, 'build_tools', 'extra-hooks')],  # Caminho para o diretório de hooks
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Use False se você quiser um executável GUI (sem console)
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app'
)
