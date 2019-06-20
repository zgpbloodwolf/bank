# -*- mode: python -*-

block_cipher = None


a = Analysis(['admis.py','userviewVer.py','sqlOperation.py','verification.py'],
             pathex=['C:\\Users\\MyPC\\PycharmProjects\\dafsdf'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas +=[('de.gif','C:\\Users\\MyPC\\PycharmProjects\\dafsdf\\de.gif','DATA'),('zhu.gif','C:\\Users\\MyPC\\PycharmProjects\\dafsdf\\zhu.gif','DATA'),('oth.gif','C:\\Users\\MyPC\\PycharmProjects\\dafsdf\\oth.gif','DATA'),('uservie.gif','C:\\Users\\MyPC\\PycharmProjects\\dafsdf\\uservie.gif','DATA')]
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='admis',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='admis')
