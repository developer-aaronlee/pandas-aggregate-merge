import pandas as pd
import matplotlib.pyplot as plt

color_df = pd.read_csv("data/colors.csv")
# print(color_df.head())
# print(color_df.shape)

unique_color = color_df["name"].nunique()
# print(unique_color)

"""Find the number of transparent colours where is_trans == 't' versus the number of opaque colours where is_trans == 'f'."""
is_trans = color_df.groupby(color_df["is_trans"]).count()
# is_trans = color_df["is_trans"].value_counts()
# print(is_trans)

sets_df = pd.read_csv("data/sets.csv")
# print(sets_df.head())
# print(sets_df.tail())

"""In which year were the first LEGO sets released and what were these sets called?"""
first_lego = sets_df.sort_values("year").head()
# print(first_lego)

"""How many different sets did LEGO sell in their first year? How many types of LEGO products were on offer in the year the company started?"""
first_year = sets_df[sets_df["year"] == 1949]
# print(first_year)

"""Find the top 5 LEGO sets with the most number of parts."""
most_parts = sets_df.sort_values("num_parts", ascending=False).head()
# print(most_parts)

"""How do the number of sets released in 1955 compare to the number of sets released in 2019?"""
sets_by_year = sets_df.groupby("year").count()
# print(sets_by_year)
# print(sets_by_year.index)

# print(sets_by_year["set_num"].head())
# print(sets_by_year["set_num"].tail())

"""Alternative solutions: get cell values"""
# Using loc[]. Get cell value by name & index
# loc_get_value = sets_by_year.loc[1949]["set_num"]
loc_get_value = sets_by_year.loc[1949][0]
# print(loc_get_value)

# Using iloc[]. Get cell value by index & name
# iloc_get_value = sets_by_year.iloc[0]["set_num"]
iloc_get_value = sets_by_year.iloc[0, 0]
# print(iloc_get_value)

# Using DataFrame.at[]
# at_get_value = sets_by_year.at[1949, "set_num"]
at_get_value = sets_by_year.at[sets_by_year.index[0], "set_num"]
# print(at_get_value)

# Using DataFrame.iat[]
iat_get_value = sets_by_year.iat[0, 0]
# print(iat_get_value)

# Get a cell value
get_cell_value = sets_by_year["set_num"].values[0]
# print(get_cell_value)

# Get cell value from last row
# last_row_cell = sets_by_year.iloc[-1]["set_num"]
# last_row_cell = sets_by_year.iloc[-1, 0]
last_row_cell = sets_by_year.at[sets_by_year.index[-1], "set_num"]
# print(loc_get_value)

"""Alternative solutions: get values and slice dataframes"""
all_col_df = sets_by_year.loc[[1955, 2019]]
# print(all_col_df)
# print(type(all_col_df))

one_col_df = sets_by_year.loc[[1955, 2019], :"set_num"]
# print(one_col_df)

two_col_df = sets_by_year.loc[[1955, 2019], ["set_num", "num_parts"]]
# print(two_col_df)

"""Show the number of LEGO releases on a line chart using Matplotlib."""
# plt.plot(sets_by_year.index, sets_by_year.set_num)
# plt.show()

# plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
# plt.show()

"""Aggregate Data with the Python .agg() Function"""
themes_by_year = sets_df.groupby("year").agg({"theme_id": pd.Series.nunique})
# print(themes_by_year.head())

themes_by_year.rename(columns={"theme_id": "nr_themes"}, inplace=True)
# print(themes_by_year.head())

"""Plot the number of themes released by year on a line chart. Only include the full calendar years (i.e., exclude 2020 and 2021)."""
# plt.plot(themes_by_year.index[:-2], themes_by_year["nr_themes"][:-2])
# plt.show()

"""Line Charts with Two Seperate Axes"""
# plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
# plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
# plt.show()

# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color="orange")
# ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color="blue")
#
# ax1.set_xlabel("Year")
# ax1.set_ylabel("Number of Sets", color="orange")
# ax2.set_ylabel("Number of Themes", color="blue")
# plt.show()

"""How many parts did the average LEGO set released in 1954 compared to say, 2017?"""
parts_per_set = sets_df.groupby("year").agg({"num_parts": pd.Series.mean})
# print(parts_per_set)
# print(parts_per_set.head())
# print(parts_per_set.tail())

"""Scatter Plots in Matplotlib"""
# plt.scatter(parts_per_set.index[:-2], parts_per_set["num_parts"][:-2])
# plt.show()

"""Which theme has the largest number of individual sets?"""
set_theme_count = sets_df["theme_id"].value_counts()
# print(set_theme_count.iloc[:10])

"""Database Schemas, Foreign Keys and Merging DataFrames"""
theme_df = pd.read_csv("data/themes.csv")
# print(theme_df.head())

"""Search for the name 'Star Wars'. How many ids correspond to this name in the themes.csv? """
starwar_ids = theme_df[theme_df["name"] == "Star Wars"]
# print(starwar_ids)

""" Now use these ids and find the corresponding the sets in the sets.csv"""
starwar_18 = sets_df[sets_df["theme_id"] == 18]
# print(starwar_18)

starwar_209 = sets_df[sets_df["theme_id"] == 209]
# print(starwar_209)

"""Merging (i.e., Combining) DataFrames based on a Key"""
# initial datatype: series
# print(set_theme_count)
# print(type(set_theme_count))

set_theme_count = pd.DataFrame(data={"id": set_theme_count.index, "set_count": set_theme_count.values})
# print(set_theme_count.head())

merged_df = pd.merge(set_theme_count, theme_df, on="id")
# print(merged_df.iloc[:10])

"""Bar Charts in Matplotlib"""
# plt.bar(merged_df["name"][:10], merged_df["set_count"][:10])
# plt.show()

# plt.figure(figsize=(12, 8))
# plt.xticks(fontsize=12, rotation=45)
# plt.yticks(fontsize=12)
# plt.ylabel('Nr of Sets', fontsize=12)
# plt.xlabel('Theme Name', fontsize=12)
#
# plt.bar(merged_df["name"][:10], merged_df["set_count"][:10])
# plt.show()
