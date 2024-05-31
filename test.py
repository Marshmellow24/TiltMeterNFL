import string
import contractions

text = "so he's saying he'll play week 1...\n\nis that..."

text = contractions.fix(text)

print(text)

ans = text.translate(str.maketrans("","", string.punctuation))

ans = " ".join(ans.split())

print(ans)