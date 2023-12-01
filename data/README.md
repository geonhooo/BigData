# 데이터 수집

-공공데이터 포털 (https://www.data.go.kr/)

-소상공인시장진흥공단_상가(상권)정보 (https://www.data.go.kr/data/15083033/fileData.do) csv 파일 수집

## 서울특별시와 편의점인 경우만 추출된 데이터프레임에서 상호명에 'GS25' 또는 '지에스'가 포함되어있는 경우만 추출
    df_seoul_gs25 = df_store[df_store['상권업종소분류명'].str.contains('편의점')&df_store['상호명'].str.contains('GS25|지에스')]
    df_seoul_gs25.index = range(len(df_seoul_gs25))
    print('서울시 내 GS25 편의점 점포 수 :', len(df_seoul_gs25))


## 서울시에 구 별로 편의점의 점포 수 구분 후 출력
    gs25_gu = df_seoul_gs25.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
    gs25_gu = gs25_gu.reset_index()
    gs25_gu = gs25_gu.set_index('시군구명')
    gs25_gu

## CU 편의점
    df_seoul_cu = df_store[df_store['상권업종소분류명'].str.contains('편의점')&df_store['상호명'].str.contains('CU|씨유')]
    df_seoul_cu.index = range(len(df_seoul_cu))
    print('서울시 내 CU 편의점 점포 수 :', len(df_seoul_cu))

## 세븐일레븐 편의점
    df_seoul_seven = df_store[df_store['상권업종소분류명'].str.contains('편의점')&df_store['상호명'].str.contains('eleven|세븐')]
    df_seoul_seven.index = range(len(df_seoul_seven))
    print('서울시 내 세븐일레븐 편의점 점포 수 :', len(df_seoul_seven))

## 미니스톱 편의점
    df_seoul_ministop = df_store[df_store['상권업종소분류명'].str.contains('편의점')&df_store['상호명'].str.contains('미니스톱')]
    df_seoul_ministop.index = range(len(df_seoul_ministop))
    print('서울시 내 미니스톱 편의점 점포 수 :', len(df_seoul_ministop))

## 이마트24 편의점
    df_seoul_emart = df_store[df_store['상권업종소분류명'].str.contains('편의점')&df_store['상호명'].str.contains('emart|이마트24')]
    df_seoul_emart.index = range(len(df_seoul_emart))
    print('서울시 내 이마트24 편의점 점포 수 :', len(df_seoul_emart))
