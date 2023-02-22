#! /bin/bash
#
#
#
if [ 8 -gt 62 ] && [ 10 -eq 10 ];
then
echo "Conditions are true"
else
echo 'error'
fi

ay='str-yu'
if [[ $ay =~ .*yu.* ]]; then
echo 'yes'
else
echo 'no'
fi

STR='GNU/Linux is an operating system'
SUB='Linux'
#if [[ $VAR =~ .*Linux.* ]]; then
if [[ "$STR" == *"$SUB"* ]]; then
  echo "It's there."
fi

for i in `ls`
do  
if [[ $i =~ .*-.* ]]; then
mv $i  ${i/-/_}
else
echo 'no'
fi
done
