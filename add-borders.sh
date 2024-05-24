# Exit on error
set -e

PICTURE_FILE="$1"
RADIUS=25

ROUNDED_FILE=${PICTURE_FILE%.*}-rounded.${PICTURE_FILE##*.}
ORIGINAL_FILE=${PICTURE_FILE%.*}-original.${PICTURE_FILE##*.}

convert $PICTURE_FILE \
  \( +clone  -alpha extract \
    -draw "fill black polygon 0,0 0,$RADIUS $RADIUS,0 fill white circle $RADIUS,$RADIUS $RADIUS,0" \
    \( +clone -flip \) -compose Multiply -composite \
    \( +clone -flop \) -compose Multiply -composite \
  \) -alpha off -compose CopyOpacity -composite $ROUNDED_FILE

# Save the original file
mv $PICTURE_FILE $ORIGINAL_FILE

convert $ROUNDED_FILE \( +clone -background black -shadow 75x10+5+5 \) +swap -bordercolor none -border 5 -background none -layers merge +repage $PICTURE_FILE

echo "Saved rounded and shaded image to $PICTURE_FILE"
echo "Original file still available as $ORIGINAL_FILE"

rm $ROUNDED_FILE
