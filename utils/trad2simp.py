from opencc import OpenCC


def trad2simp(
        text: str
):
    return OpenCC('t2s').convert(text)
