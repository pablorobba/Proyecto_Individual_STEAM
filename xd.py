grouped = df_first_query.groupby('year')  #first, we group

total_count_by_year = grouped['items_count'].sum()

zero_price_count_by_year = grouped.apply(lambda group: (group['price'] == 0).sum())
percentage_zero_price_by_year = (zero_price_count_by_year / total_count_by_year) * 100
df_first_query = pd.DataFrame({
    'Total Items': total_count_by_year,
    'Zero Price Items': zero_price_count_by_year,
    'Percentage of Zero Price': percentage_zero_price_by_year
})
