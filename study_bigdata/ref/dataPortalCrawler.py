import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd
import pymysql

ServiceKey="Ody77GLuYeR%2FeFqbpduMN2Bi4Cka2fztbgnj6E2Eux1kUhy3e4epR28XKBUaObiqPoVzAizxXMBPXtMyuC9v9Q%3D%3D"

#[CODE 1]
def getRequestUrl(url):    
    req = urllib.request.Request(url)    
    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}] Url Request Success')
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f'[{datetime.datetime.now()}] Error for URL : {url}')
        return None


#[CODE 2]
def getTourismStatsItem(yyyymm, national_code, ed_cd):    
    service_url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    parameters = f'?_type=json&serviceKey={ServiceKey}'   #인증키
    parameters += f'&YM={yyyymm}'
    parameters += f'&NAT_CD={national_code}'
    parameters += f'&ED_CD={ed_cd}'
    url = service_url + parameters
    
    retData = getRequestUrl(url)   #[CODE 1]
    
    if (retData == None):
        return None
    else:
         return json.loads(retData)

#[CODE 3]
def getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear):
    jsonResult = []
    result = []
    natName=''
    dataEND = f'{str(nEndYear)}{str(12):0>2}' #데이터 끝 초기화
    isDataEnd = 0 #데이터 끝 확인용 flag 초기화    
    
    for year in range(nStartYear, nEndYear+1):        
        for month in range(1, 13):
            if(isDataEnd == 1): break #데이터 끝 flag 설정되어있으면 작업 중지.
            yyyymm = f'{str(year)}{str(month):0>2}'           
            jsonData = getTourismStatsItem(yyyymm, nat_cd, ed_cd) #[CODE 2]
            
            if (jsonData['response']['header']['resultMsg'] == 'OK'):               
                # 입력된 범위까지 수집하지 않았지만, 더이상 제공되는 데이터가 없는 마지막 항목인 경우 -------------------
                if jsonData['response']['body']['items'] == '': 
                    isDataEnd = 1 #데이터 끝 flag 설정
                    dataEND = "{0}{1:0>2}".format(str(year), str(month-1))
                    print(f'데이터 없음.... \n 제공되는 통계 데이터는 {str(year)}년 {str(month-1)}월까지입니다.')                    
                    break                
                #jsonData를 출력하여 확인
                print (json.dumps(jsonData, indent=4, 
                         sort_keys=True, ensure_ascii=False))          
                natName = jsonData['response']['body']['items']['item']['natKorNm']
                natName = natName.replace(' ', '')
                num = jsonData['response']['body']['items']['item']['num']
                ed = jsonData['response']['body']['items']['item']['ed']
                print(f'[ {natName}_{yyyymm} : {num} ]')
                print('----------------------------------------------------------------------')                
                jsonResult.append({'nat_name': natName, 'nat_cd': nat_cd,
                                 'yyyymm': yyyymm, 'visit_cnt': num})
                result.append([natName, nat_cd, yyyymm, num])
                
    return (jsonResult, result, natName, ed, dataEND)

#[CODE 0]
def main():
    jsonResult = []
    result = []
    natName=''
    print("<< 국내 입국한 외국인의 통계 데이터를 수집합니다. >>")
    nat_cd = input('국가 코드를 입력하세요(중국: 112 / 일본: 130 / 미국: 275) : ')
    nStartYear =int(input('데이터를 몇 년부터 수집할까요? : '))
    nEndYear = int(input('데이터를 몇 년까지 수집할까요? : '))
    ed_cd = "E"     #E : 방한외래관광객, D : 해외 출국
    
    jsonResult, result, natName, ed, dataEND =getTourismStatsService(nat_cd,
                                            ed_cd, nStartYear, nEndYear) #[CODE 3]

    if (natName=='') : #URL 요청은 성공하였지만, 데이터 제공이 안된 경우
        print('데이터가 전달되지 않았습니다. 공공데이터포털의 서비스 상태를 확인하기 바랍니다.')
    else:
        #파일저장 1 : json 파일       
        with open('./%s_%s_%d_%s.json' % (natName, ed, nStartYear, dataEND), 'w', 
                    encoding='utf8') as outfile:
            jsonFile  = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(jsonFile)
        #파일저장 2 : csv 파일   
        columns = ["입국자국가", "국가코드", "입국연월", "입국자 수"]
        result_df = pd.DataFrame(result, columns = columns)
        result_df.to_csv('./%s_%s_%d_%s.csv' % (natName, ed, nStartYear, dataEND),
                    index=False, encoding='cp949')
        # DB저장 :
        columns = ['nat_name', 'nat_cd', 'yyyymm', 'visit_cnt']
        result_df = pd.DataFrame(result, columns = columns)
        
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                user='root',
                                password='mysql_p@ssw0rd',
                                db='crawling_data')
        
        # create cursor
        cursor=connection.cursor()
        
        # creating column list for insertion
        cols = "`,`".join([str(i) for i in result_df.columns.tolist()])
        
        # Insert DataFrame recrds one by one.
        for i,row in result_df.iterrows():
            sql = "INSERT INTO `tourist_sumary` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
            cursor.execute(sql, tuple(row))

            # the connection is not autocommitted by default, so we must commit to save our changes
            connection.commit()
        
    
if __name__ == '__main__':
    main()
