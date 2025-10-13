# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file cho VPN Connection Tool
Build thành file .exe standalone với tất cả dependencies
"""

block_cipher = None

a = Analysis(
    ['main_gui.py'],  # Entry point
    pathex=[],
    binaries=[],
    datas=[
        ('config.yaml', '.'),  # Include config file
    ],
    hiddenimports=[
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
        'requests',
        'yaml',
        'psutil',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'PIL',
        'tkinter',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='VPN_Connection_Tool',  # Tên file .exe
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Nén với UPX để file nhỏ hơn
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Không hiện console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Có thể thêm icon sau: icon='icon.ico'
    uac_admin=True,  # Yêu cầu quyền admin khi chạy
    uac_uiaccess=False,
)
