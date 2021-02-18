BG=unset
FG=unset
SHORT_OPTIONS=""
LONG_OPTIONS=""
LONG_OPTIONS="${LONG_OPTIONS},bg:"
LONG_OPTIONS="${LONG_OPTIONS},fg:"
PARSED_ARGUMENTS=$(getopt -o "${SHORT_OPTIONS}" --long $LONG_OPTIONS -- "$@")

print_usage()
{
    echo "JOHN
	MARIA"
    exit 2
}

VALID_ARGUMENTS=$?
if [ "$VALID_ARGUMENTS" != "0" ]; then
    print_usage
fi

eval set -- "$PARSED_ARGUMENTS"
while :
do
    case "$1" in
        --bg) BG="$2"; shift 2 ;;
        --fg) FG="$2"; shift 2 ;;
        --) shift; break ;;
        *) print_usage ;;
    esac
done

echo "BG = $BG"
