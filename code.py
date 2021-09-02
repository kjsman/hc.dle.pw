def fix_font():
    # From https://HC.Dle.pw, By Jinseo Kim
    # Licensed by The Unlicense (https://unlicense.org)
    # v1.0.0
    import os
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    os.system("apt-get install -y fonts-nanum")
    os.system("fc-cache -fv")
    mpl.font_manager._rebuild()
    mpl.font_manager.findfont = mpl.font_manager.fontManager.findfont
    mpl.backends.backend_agg.findfont = mpl.font_manager.fontManager.findfont
    plt.rcParams['font.family'] = "NanumBarunGothic"
    plt.rcParams['axes.unicode_minus'] = False

fix_font()