#!/bin/bash
EDITOR="subl"
TITLE="$*"

while [ -z "$TITLE" ];
do
    echo -n "please input the title:";
    read TITLE
done

# echo -n "please input the categories:"; read categories

# if [ -z "$categories" ];
#     then categories="Uncategorized"
# fi

POST=$(echo $TITLE | sed -r 's/[a-z]+>/\u&/g')
FILE=$(date "+./_posts/%Y-%m-%d-${TITLE}.md" | sed -e y/\ /-/)

echo "---" >> $FILE
echo "title: \"$POST\"" >> $FILE
echo "layout: post" >> $FILE
echo "categories:" >> $FILE
echo " - Uncategorized" >> $FILE
echo "---" >> $FILE

$EDITOR $FILE
