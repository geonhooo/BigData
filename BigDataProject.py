# -*- coding: utf-8 -*-
"""Untitled23.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1liJ-xfYieuYZUhppFYTexT0jhWYB8NAn
"""

import folium
import json
import glob
import os
import pandas as pd
import numpy as np

#공공데이터 포털에서 수집한 서울시에 있는 상가(상권)정보 변환
df = pd.read_csv('/content/drive/MyDrive/소상공인시장진흥공단_상가(상권)정보_서울_202309.csv', engine='python', encoding='utf-8')

#필요한 열만 지정하여 새로 dataset 만들기
dataset = df[['상호명','지점명',
              '상권업종소분류명',
              '시도명', '시군구명', '행정동명',
              '위도', '경도']]

#상권업종소분류명이 '편의점' 이면서 시도명이 '서울특별시'인 경우만 추출
df_store = dataset[(dataset['상권업종소분류명']=='편의점')&(dataset['시도명']=='서울특별시')]


#상가(상권)정보에서 '상권업종소분류명' 열에 '편의점' 으로 필터링하여 편의점으로 분류되어있는 상권 수 확인
df_seoul_store = df_store[df_store['상권업종소분류명'].str.contains('편의점')]
df_seoul_store.index = range(len(df_seoul_store))
print('서울시 내 편의점 점포 수 :', len(df_seoul_store))


#서울시에 구 별로 편의점의 점포 수 구분 후 출력
store_gu = df_seoul_store.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
store_gu = store_gu.reset_index()
store_gu = store_gu.set_index('시군구명')
store_gu

# 서울특별시와 편의점인 경우만 추출된 데이터프레임에서 상호명에 'GS25' 또는 '지에스'가 포함되어있는 경우만 추출
df_seoul_gs25 = df_store[df_store['상권업종소분류명'].str.contains('편의점')&df_store['상호명'].str.contains('GS25|지에스')]
df_seoul_gs25.index = range(len(df_seoul_gs25))
print('서울시 내 GS25 편의점 점포 수 :', len(df_seoul_gs25))


#서울시에 구 별로 편의점의 점포 수 구분 후 출력
gs25_gu = df_seoul_gs25.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
gs25_gu = gs25_gu.reset_index()
gs25_gu = gs25_gu.set_index('시군구명')
gs25_gu

# 서울특별시와 편의점인 경우만 추출된 데이터프레임에서 상호명에 'CU' 또는 '씨유'가 포함되어있는 경우만 추출
df_seoul_cu = df_store[df_store['상권업종소분류명'].str.contains('편의점')&df_store['상호명'].str.contains('CU|씨유')]
df_seoul_cu.index = range(len(df_seoul_cu))
print('서울시 내 CU 편의점 점포 수 :', len(df_seoul_cu))


#서울시에 구 별로 편의점의 점포 수 구분 후 출력
cu_gu = df_seoul_cu.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
cu_gu = cu_gu.reset_index()
cu_gu = cu_gu.set_index('시군구명')
cu_gu

# 세븐일레븐 편의점
df_seoul_seven = df_store[df_store['상권업종소분류명'].str.contains('편의점')&df_store['상호명'].str.contains('eleven|세븐')]
df_seoul_seven.index = range(len(df_seoul_seven))
print('서울시 내 세븐일레븐 편의점 점포 수 :', len(df_seoul_seven))


#서울시에 구 별로 편의점의 점포 수 구분 후 출력
seven_gu = df_seoul_seven.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
seven_gu = seven_gu.reset_index()
seven_gu = seven_gu.set_index('시군구명')
seven_gu

# 미니스톱 편의점
df_seoul_ministop = df_store[df_store['상권업종소분류명'].str.contains('편의점')&df_store['상호명'].str.contains('미니스톱')]
df_seoul_ministop.index = range(len(df_seoul_ministop))
print('서울시 내 미니스톱 편의점 점포 수 :', len(df_seoul_ministop))


#서울시에 구 별로 편의점의 점포 수 구분 후 출력
ministop_gu = df_seoul_ministop.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
ministop_gu = ministop_gu.reset_index()
ministop_gu = ministop_gu.set_index('시군구명')
ministop_gu

# 이마트24 편의점
df_seoul_emart = df_store[df_store['상권업종소분류명'].str.contains('편의점')&df_store['상호명'].str.contains('emart|이마트24')]
df_seoul_emart.index = range(len(df_seoul_emart))
print('서울시 내 이마트24 편의점 점포 수 :', len(df_seoul_emart))


#서울시에 구 별로 편의점의 점포 수 구분 후 출력
emart_gu = df_seoul_emart.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
emart_gu = emart_gu.reset_index()
emart_gu = emart_gu.set_index('시군구명')
emart_gu

#대한민국 지리정보 파일
geo_path = '/content/drive/MyDrive/02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

# 위치 파라미터 설정
loc = [37.5502, 126.982] # 위도(N), 경도(E)

#서울시 편의점 수
size_store = len(df_seoul_store)
#size_gs25 = len(df_seoul_gs25)
#size_cu = len(df_seoul_cu)
#size_seven = len(df_seoul_seven)
#size_ministop = len(df_seoul_ministop)
#size_emart = len(df_seoul_emart)

# 서울시 편의점 전체 지도
map_store = folium.Map(location=loc, zoom_start=12)
map_store.choropleth(geo_data=geo_str,
              data = store_gu['상호명'],
              columns=[store_gu.index, store_gu['상호명']],
              fill_color='PuRd',
              key_on='feature.id')


# 포인트 마커 추가

for i in range(size_store):

    folium.Marker(list(df_seoul_store.iloc[i][['위도', '경도']]),
                 popup=df_seoul_store.iloc[i][['상호명']],
                 icon=folium.Icon(color='gray')).add_to(map_store)

map_store

# 위치 파라미터 설정
loc = [37.5502, 126.982] # 위도(N), 경도(E)

#서울시 편의점 수
size_gs25 = len(df_seoul_gs25)
size_cu = len(df_seoul_cu)
size_seven = len(df_seoul_seven)
size_ministop = len(df_seoul_ministop)
size_emart = len(df_seoul_emart)

# 서울시 편의점 전체 지도
map_store = folium.Map(location=loc, zoom_start=12)
map_store.choropleth(geo_data=geo_str,
              data = store_gu['상호명'],
              columns=[store_gu.index, store_gu['상호명']],
              fill_color='PuRd',
              key_on='feature.id')


# 포인트 마커 추가

for i in range(size_gs25):

    folium.Marker(list(df_seoul_gs25.iloc[i][['위도', '경도']]),
                 popup=df_seoul_gs25.iloc[i][['상호명']],
                 icon=folium.Icon(color='blue')).add_to(map_store)

for i in range(size_cu):

    folium.Marker(list(df_seoul_cu.iloc[i][['위도', '경도']]),
                 popup=df_seoul_cu.iloc[i][['상호명']],
                 icon=folium.Icon(color='green')).add_to(map_store)

for i in range(size_emart):

    folium.Marker(list(df_seoul_emart.iloc[i][['위도', '경도']]),
                 popup=df_seoul_emart.iloc[i][['상호명']],
                 icon=folium.Icon(color='purple')).add_to(map_store)

for i in range(size_ministop):

    folium.Marker(list(df_seoul_ministop.iloc[i][['위도', '경도']]),
                 popup=df_seoul_ministop.iloc[i][['상호명']],
                 icon=folium.Icon(color='beige')).add_to(map_store)

for i in range(size_seven):

    folium.Marker(list(df_seoul_seven.iloc[i][['위도', '경도']]),
                 popup=df_seoul_seven.iloc[i][['상호명']],
                 icon=folium.Icon(color='orange')).add_to(map_store)





map_store