import keyboard
import time

time.sleep(10)

toType = "Rhubarb is a general term used for the cultivated plants in the genus Rheum in the family Polygonaceae.[2] It is a herbaceous perennial growing from short, thick rhizomes. Historically, different plants have been called rhubarb in English. The fleshy, edible stalks (petioles) of other species and hybrids (culinary rhubarb) were cooked and used for food. The large, triangular leaves contain high levels of oxalic acid, and anthrone glycosides making them inedible. The small flowers are grouped in large compound leafy greenish-white to rose-red inflorescences. The precise origin of culinary rhubarb is unknown. The species Rheum rhabarbarum (syn. R. undulatum) and R. rhaponticum were grown in Europe before the 18th century and used for medicinal purposes. By the early 18th century, these two species and a possible hybrid of unknown origin, R.  hybridum, were grown as vegetable crops in England and Scandinavia. They readily hybridize, and culinary rhubarb was developed by selecting open-pollinated seed, so that its precise origin is almost impossible to determine.[3] In appearance, culinary rhubarb varies continuously between R. rhaponticum and R. rhabarbarum. However, modern rhubarb cultivars are tetraploids with 2n = 44, in contrast to 2n = 22 for the wild species.[4] Although rhubarb is a vegetable, it is often put to the same culinary uses as fruits.[5] The leaf stalks can be used raw, when they have a crisp texture (similar to celery, although it is in a different family), but are most commonly cooked with sugar and used in pies, crumbles and other desserts. They have a strong, tart taste. Many cultivars have been developed for human consumption, most of which are recognised as Rheum  hybridum by the Royal Horticultural Society.[6]"
wordsToType = []
hold_i = 0 # last index of a space
for i in range(len(toType)):
    if toType[i] == " ":
        wordsToType.append(toType[hold_i: i])
        hold_i = i+1

t1 = time.time()
duration = 600
while( t1 + duration > time.time()):
    for word in wordsToType:
        keyboard.write(word)
        keyboard.press_and_release('return')

