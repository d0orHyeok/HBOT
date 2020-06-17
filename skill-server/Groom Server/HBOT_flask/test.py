from flask import Flask, request, jsonify
import sys
app = Flask(__name__)


@app.route('/message', methods=['POST'])
def Message():
    
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']
    
    if content != u"안녕":
        dataSend = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "코로나 관련 뉴스입니다!",
            "imageUrl": "corona.jpg"
          },
          "items": [
            {
              "title": "Kakao i Developers",
              "description": "새로운 AI의 내일과 일상의 변화",
              "imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
              "link": {
                "web": "https://namu.wiki/w/%EB%9D%BC%EC%9D%B4%EC%96%B8(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
              }
            },
            {
              "title": "Kakao i Open Builder",
              "description": "카카오톡 채널 챗봇 만들기",
              "imageUrl": "http://k.kakaocdn.net/dn/N4Epz/btqqHCfF5II/a3kMRckYml1NLPEo7nqTmK/1x1.jpg",
              "link": {
                "web": "https://namu.wiki/w/%EB%AC%B4%EC%A7%80(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
              }
            },
            {
              "title": "Kakao i Voice Service",
              "description": "보이스봇 / KVS 제휴 신청하기",
              "imageUrl": "http://k.kakaocdn.net/dn/bE8AKO/btqqFHI6vDQ/mWZGNbLIOlTv3oVF1gzXKK/1x1.jpg",
              "link": {
                "web": "https://namu.wiki/w/%EC%96%B4%ED%94%BC%EC%B9%98"
              }
            }
          ],
          "buttons": [
            {
              "label": "구경가기",
              "action": "webLink",
              "webLinkUrl": "https://namu.wiki/w/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88"
            }
          ]
        }
      }
    ]
 
  }
}
    
    return jsonify(dataSend)



if __name__ == "__main__":
    app.run(host='0.0.0.0')