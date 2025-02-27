import todoList
import boto3


def translate(event, context):
    translate = boto3.client(
                        service_name='translate',
                        region_name='us-east-1',
                        use_ssl=True)
    print("Estoy en translate")
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])
    if item:
        try:
            # result = translate.translate_text(
            #            Text=item.get('text'),
            #            SourceLanguageCode="auto",
            #            TargetLanguageCode=event['pathParameters']['language'])
            result = todoList.translate_item(
                                    item.get('text'),
                                    event['pathParameters']['language'],
                                    translate)
            response = {
                "statusCode": 200,
                "body": result.get('TranslatedText')
            }
        except Exception as e:
            print('Estoy en la excepcion')
            print(e)
            response = {
                "statusCode": 400,
                "body": str(e)
            }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
