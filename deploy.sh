for VAR in API_KEY APP_ID
do
    if [[ -z ${!VAR+x} ]]; then
        echo "env variable" $VAR "missing"
        exit 1
    fi
done

rsconnect deploy dash \
    --entrypoint run.app:app \
    --server https://rsc.ds.umcutrecht.nl/ \
    --api-key $API_KEY \
    --app-id $APP_ID \
    .
