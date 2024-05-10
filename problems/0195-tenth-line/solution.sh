# Read from the file file.txt and output the tenth line to stdout.
current=0
while read -r line; do
    current=$((current + 1))
    if [[ $current -eq 10 ]]; then
        echo $line
    fi
done < "file.txt"
