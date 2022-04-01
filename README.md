README

txt2JSON, in its current form, is a python program that takes a newline (\n) delimited text file, converts it to a dictionary, and adds the values of the keys to a list of dictionaries based on matching keys.

For example:

	JSON file before modification (imported as list of dictionaries):

	[{
	"STATES":"Alabama",
	"CAPITALS":"Montgomery",
	"POPULATION":"4858979",
	"AREA":"52419"
	},

	{
	"STATES":"Alaska",
	"CAPITALS":"Juneau",
	"POPULATION":"738432",
	"AREA":"663267"
	},
	{
	"STATES":"Arizona",
	"CAPITALS":"Phoenix",
	"POPULATION":"6828065",
	"AREA":"113998"},

	{
	"STATES":"Arkansas",
	"CAPITALS":"Little Rock",
	"POPULATION":"2978204",
	"AREA":"53179"
	},

	{
	"STATES":"California",
	"CAPITALS":"Sacramento",
	"POPULATION":"39144818","AREA":"163696"
	}]

	.TXT file with data to be appended to JSON file (sorting is unnecessary, must follow key1 \n value1 \n key45 \n value45 format):

	Alabama							KEY1
	Dec. 14, 1819					VALUE1
	Alaska							KEY2
	Jan. 3, 1959					VALUE2
	Arizona							KEY3
	Feb. 14, 1912					VALUE3...
	Arkansas
	June 15, 1836
	California
	Sept. 9, 1850


	FINAL PRODUCT (Key name is manually entered at runtime. "DATE" is used here.)
	[{
	"STATES":"Alabama",
	"CAPITALS":"Montgomery",
	"POPULATION":"4858979",
	"AREA":"52419"
	"DATE": "Dec. 14, 1819"
	},

	{
	"STATES":"Alaska",
	"CAPITALS":"Juneau",
	"POPULATION":"738432",
	"AREA":"663267"
	"DATE": "Jan 3, 1959"
	},
	{
	"STATES":"Arizona",
	"CAPITALS":"Phoenix",
	"POPULATION":"6828065",
	"AREA":"113998"},
	"DATE":"Feb 14, 1912"

	{
	"STATES":"Arkansas",
	"CAPITALS":"Little Rock",
	"POPULATION":"2978204",
	"AREA":"53179"
	"YEAR":"June 15, 1836"
	},

	{
	"STATES":"California",
	"CAPITALS":"Sacramento",
	"POPULATION":"39144818",
	"AREA":"163696"
	"YEAR":"Sept. 9, 1850"
	}]