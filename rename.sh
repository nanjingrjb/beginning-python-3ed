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
   if [[ $i =~ .*Chapter.* ]];
   then
	   echo 'enter dir ' $i
	   cd ./$i
	   for j in `ls`
            do
		    if [[ $j =~ .*-.* ]]; then
                    mv $j  ${j/-/_}
		    #echo ${j/-/_}
                    fi
            done
	    cd ../
   fi	    
done
