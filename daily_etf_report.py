# daily_etf_report.py
from datetime import datetime

def get_etf_data():
    """ETF 비중 변화 데이터 (실제로는 MCP나 API로 연결)"""
    today = datetime.now().strftime("%Y년 %m월 %d일")
    
    report = f"""📊 {today} ETF 비중 변화 리포트

🔥 가장 많이 비중 증가한 종목 Top 3

1. 삼성SDI (+4.11%p)
   - TIME 코스피액티브에서 가장 큰 증가
   - 2차전지 강세

2. 엘앤에프 (신규 편입)
   - TIME 코스피액티브, TIGER 코리아테크액티브 모두 편입

3. 효성중공업 (+2.52%p)
   - 산업재 섹터 강세

📌 오늘의 추천
• TIME 코스피액티브: 2차전지 로테이션 중
• TIGER 코리아테크액티브: 테크 집중 유지

(실제 데이터는 MCP 연결 시 자동 업데이트됩니다)
"""
    return report

def send_to_kakaotalk(message):
    """카카오톡으로 메시지 보내기 (실제 키 필요)"""
    print("=== 카카오톡으로 전송되는 내용 ===")
    print(message)
    print("===================================")
    # 실제로는 여기서 Kakao API 호출 코드가 들어갑니다.

if __name__ == "__main__":
    report = get_etf_data()
    send_to_kakaotalk(report)
