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
    hooksconfig={
        # Disable conda support để tránh MemoryError
        'conda': {'enabled': False},
    },
    runtime_hooks=[],
    excludes=[
        # === Data Science & ML (KHÔNG CẦN) ===
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'sklearn',
        'tensorflow',
        'torch',
        'keras',

        # === GUI Frameworks Khác (KHÔNG CẦN) ===
        'tkinter',
        'wx',
        'PySide2',
        'PySide6',
        'PyQt6',

        # === Development Tools (KHÔNG CẦN) ===
        'IPython',
        'jupyter',
        'notebook',
        'jupyterlab',
        'sphinx',
        'pytest',
        'unittest',
        'doctest',
        'pdb',
        'pydoc',

        # === Build Tools (KHÔNG CẦN SAU KHI BUILD) ===
        'setuptools',
        'wheel',
        'pip',
        'distutils',
        'pkg_resources',

        # === Image Processing (KHÔNG CẦN) ===
        'PIL',
        'Pillow',
        'cv2',
        'imageio',

        # === Web Frameworks (KHÔNG CẦN) ===
        'flask',
        'django',
        'fastapi',
        'tornado',

        # === Database (KHÔNG CẦN) ===
        'sqlalchemy',
        'sqlite3',
        'pymongo',
        'redis',

        # === Cryptography Submodules (KHÔNG CẦN) ===
        'cryptography.hazmat.primitives.asymmetric.x25519',
        'cryptography.hazmat.primitives.asymmetric.x448',
        'cryptography.hazmat.primitives.asymmetric.ed25519',
        'cryptography.hazmat.primitives.asymmetric.ed448',

        # === Other Unused (KHÔNG CẦN) ===
        'xml',
        'xmlrpc',
        'email',
        'multiprocessing',
        'asyncio',
        'concurrent',
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
