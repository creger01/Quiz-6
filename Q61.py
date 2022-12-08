#Cadyn Reger
import dbm
photo_category = dbm.open("captions", "c")
photo_category["sunsets.png"] = "beautiful colors in the sky"
photo_category["friends.png"] = "my biggest supporters in my life"
photo_category["dogs.png"] = "the friendliest animal to exitst"

for item in photo_category:
    print(item, photo_category[item])

# b'sunsets.png' b'beautiful colors in the sky'
# b'friends.png' b'my biggest supporters in my life'
# b'dogs.png' b'the friendliest animal to exitst'
