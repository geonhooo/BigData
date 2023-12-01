loc = [37.5502, 126.982] # 위도(N), 경도(E)


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
