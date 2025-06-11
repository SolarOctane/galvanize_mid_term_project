{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bf754924",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Libraries\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import matplotlib as mpl\n",
    "import matplotlib.ticker as mticker\n",
    "import matplotlib.dates as mdates\n",
    "import matplotlib\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6e2dc502",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Fiscal Year</th>\n",
       "      <th>Month Grouping</th>\n",
       "      <th>Month (abbv)</th>\n",
       "      <th>Component</th>\n",
       "      <th>Land Border Region</th>\n",
       "      <th>Area of Responsibility</th>\n",
       "      <th>AOR (Abbv)</th>\n",
       "      <th>Demographic</th>\n",
       "      <th>Citizenship</th>\n",
       "      <th>Title of Authority</th>\n",
       "      <th>Encounter Type</th>\n",
       "      <th>Encounter Count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>FYTD</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Inadmissibles</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>FYTD</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>MEXICO</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>FYTD</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021</td>\n",
       "      <td>FYTD</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Single Adults</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021</td>\n",
       "      <td>FYTD</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Single Adults</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Inadmissibles</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58739</th>\n",
       "      <td>2024</td>\n",
       "      <td>FYTD</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>GUATEMALA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58740</th>\n",
       "      <td>2024</td>\n",
       "      <td>FYTD</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>MEXICO</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58741</th>\n",
       "      <td>2024</td>\n",
       "      <td>FYTD</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58742</th>\n",
       "      <td>2024</td>\n",
       "      <td>FYTD</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>RUSSIA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58743</th>\n",
       "      <td>2024</td>\n",
       "      <td>FYTD</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>VENEZUELA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>58744 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       Fiscal Year Month Grouping Month (abbv)                   Component  \\\n",
       "0             2021           FYTD          APR  Office of Field Operations   \n",
       "1             2021           FYTD          APR  Office of Field Operations   \n",
       "2             2021           FYTD          APR  Office of Field Operations   \n",
       "3             2021           FYTD          APR  Office of Field Operations   \n",
       "4             2021           FYTD          APR  Office of Field Operations   \n",
       "...            ...            ...          ...                         ...   \n",
       "58739         2024           FYTD          SEP          U.S. Border Patrol   \n",
       "58740         2024           FYTD          SEP          U.S. Border Patrol   \n",
       "58741         2024           FYTD          SEP          U.S. Border Patrol   \n",
       "58742         2024           FYTD          SEP          U.S. Border Patrol   \n",
       "58743         2024           FYTD          SEP          U.S. Border Patrol   \n",
       "\n",
       "          Land Border Region Area of Responsibility AOR (Abbv)  \\\n",
       "0       Northern Land Border    Boston Field Office     Boston   \n",
       "1       Northern Land Border    Boston Field Office     Boston   \n",
       "2       Northern Land Border    Boston Field Office     Boston   \n",
       "3       Northern Land Border    Boston Field Office     Boston   \n",
       "4       Northern Land Border    Boston Field Office     Boston   \n",
       "...                      ...                    ...        ...   \n",
       "58739  Southwest Land Border            Yuma Sector        YUM   \n",
       "58740  Southwest Land Border            Yuma Sector        YUM   \n",
       "58741  Southwest Land Border            Yuma Sector        YUM   \n",
       "58742  Southwest Land Border            Yuma Sector        YUM   \n",
       "58743  Southwest Land Border            Yuma Sector        YUM   \n",
       "\n",
       "              Demographic Citizenship Title of Authority Encounter Type  \\\n",
       "0      Accompanied Minors      CANADA            Title 8  Inadmissibles   \n",
       "1      Accompanied Minors      MEXICO           Title 42     Expulsions   \n",
       "2      Accompanied Minors       OTHER           Title 42     Expulsions   \n",
       "3           Single Adults      CANADA           Title 42     Expulsions   \n",
       "4           Single Adults      CANADA            Title 8  Inadmissibles   \n",
       "...                   ...         ...                ...            ...   \n",
       "58739  UC / Single Minors   GUATEMALA            Title 8  Apprehensions   \n",
       "58740  UC / Single Minors      MEXICO            Title 8  Apprehensions   \n",
       "58741  UC / Single Minors       OTHER            Title 8  Apprehensions   \n",
       "58742  UC / Single Minors      RUSSIA            Title 8  Apprehensions   \n",
       "58743  UC / Single Minors   VENEZUELA            Title 8  Apprehensions   \n",
       "\n",
       "       Encounter Count  \n",
       "0                    3  \n",
       "1                    2  \n",
       "2                    6  \n",
       "3                   11  \n",
       "4                   40  \n",
       "...                ...  \n",
       "58739               27  \n",
       "58740               76  \n",
       "58741                4  \n",
       "58742                1  \n",
       "58743                3  \n",
       "\n",
       "[58744 rows x 12 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Pandas Dataframe\n",
    "\n",
    "encounters_aor_df = pd.read_csv('.venv/nationwide-encounters-fy21-fy24-aor.csv')\n",
    "encounters_aor_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "19b976b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 58744 entries, 0 to 58743\n",
      "Data columns (total 12 columns):\n",
      " #   Column                  Non-Null Count  Dtype \n",
      "---  ------                  --------------  ----- \n",
      " 0   Fiscal Year             58744 non-null  int64 \n",
      " 1   Month Grouping          58744 non-null  object\n",
      " 2   Month (abbv)            58744 non-null  object\n",
      " 3   Component               58744 non-null  object\n",
      " 4   Land Border Region      58744 non-null  object\n",
      " 5   Area of Responsibility  58744 non-null  object\n",
      " 6   AOR (Abbv)              58744 non-null  object\n",
      " 7   Demographic             58744 non-null  object\n",
      " 8   Citizenship             58744 non-null  object\n",
      " 9   Title of Authority      58744 non-null  object\n",
      " 10  Encounter Type          58744 non-null  object\n",
      " 11  Encounter Count         58744 non-null  int64 \n",
      "dtypes: int64(2), object(10)\n",
      "memory usage: 5.4+ MB\n"
     ]
    }
   ],
   "source": [
    "# Dataframe Info\n",
    "\n",
    "encounters_aor_df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9f528ae9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Change 'Fiscal Year' column to string\n",
    "encounters_aor_df['Fiscal Year'] = encounters_aor_df['Fiscal Year'].astype(object)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "08021856",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 58744 entries, 0 to 58743\n",
      "Data columns (total 12 columns):\n",
      " #   Column                  Non-Null Count  Dtype \n",
      "---  ------                  --------------  ----- \n",
      " 0   Fiscal Year             58744 non-null  object\n",
      " 1   Month Grouping          58744 non-null  object\n",
      " 2   Month (abbv)            58744 non-null  object\n",
      " 3   Component               58744 non-null  object\n",
      " 4   Land Border Region      58744 non-null  object\n",
      " 5   Area of Responsibility  58744 non-null  object\n",
      " 6   AOR (Abbv)              58744 non-null  object\n",
      " 7   Demographic             58744 non-null  object\n",
      " 8   Citizenship             58744 non-null  object\n",
      " 9   Title of Authority      58744 non-null  object\n",
      " 10  Encounter Type          58744 non-null  object\n",
      " 11  Encounter Count         58744 non-null  int64 \n",
      "dtypes: int64(1), object(11)\n",
      "memory usage: 5.4+ MB\n"
     ]
    }
   ],
   "source": [
    "encounters_aor_df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c9ad7378",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Fiscal Year</th>\n",
       "      <th>Month (abbv)</th>\n",
       "      <th>Component</th>\n",
       "      <th>Land Border Region</th>\n",
       "      <th>Area of Responsibility</th>\n",
       "      <th>AOR (Abbv)</th>\n",
       "      <th>Demographic</th>\n",
       "      <th>Citizenship</th>\n",
       "      <th>Title of Authority</th>\n",
       "      <th>Encounter Type</th>\n",
       "      <th>Encounter Count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Inadmissibles</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>MEXICO</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Single Adults</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Single Adults</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Inadmissibles</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58739</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>GUATEMALA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58740</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>MEXICO</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58741</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58742</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>RUSSIA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58743</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>VENEZUELA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>58744 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Fiscal Year Month (abbv)                   Component  \\\n",
       "0            2021          APR  Office of Field Operations   \n",
       "1            2021          APR  Office of Field Operations   \n",
       "2            2021          APR  Office of Field Operations   \n",
       "3            2021          APR  Office of Field Operations   \n",
       "4            2021          APR  Office of Field Operations   \n",
       "...           ...          ...                         ...   \n",
       "58739        2024          SEP          U.S. Border Patrol   \n",
       "58740        2024          SEP          U.S. Border Patrol   \n",
       "58741        2024          SEP          U.S. Border Patrol   \n",
       "58742        2024          SEP          U.S. Border Patrol   \n",
       "58743        2024          SEP          U.S. Border Patrol   \n",
       "\n",
       "          Land Border Region Area of Responsibility AOR (Abbv)  \\\n",
       "0       Northern Land Border    Boston Field Office     Boston   \n",
       "1       Northern Land Border    Boston Field Office     Boston   \n",
       "2       Northern Land Border    Boston Field Office     Boston   \n",
       "3       Northern Land Border    Boston Field Office     Boston   \n",
       "4       Northern Land Border    Boston Field Office     Boston   \n",
       "...                      ...                    ...        ...   \n",
       "58739  Southwest Land Border            Yuma Sector        YUM   \n",
       "58740  Southwest Land Border            Yuma Sector        YUM   \n",
       "58741  Southwest Land Border            Yuma Sector        YUM   \n",
       "58742  Southwest Land Border            Yuma Sector        YUM   \n",
       "58743  Southwest Land Border            Yuma Sector        YUM   \n",
       "\n",
       "              Demographic Citizenship Title of Authority Encounter Type  \\\n",
       "0      Accompanied Minors      CANADA            Title 8  Inadmissibles   \n",
       "1      Accompanied Minors      MEXICO           Title 42     Expulsions   \n",
       "2      Accompanied Minors       OTHER           Title 42     Expulsions   \n",
       "3           Single Adults      CANADA           Title 42     Expulsions   \n",
       "4           Single Adults      CANADA            Title 8  Inadmissibles   \n",
       "...                   ...         ...                ...            ...   \n",
       "58739  UC / Single Minors   GUATEMALA            Title 8  Apprehensions   \n",
       "58740  UC / Single Minors      MEXICO            Title 8  Apprehensions   \n",
       "58741  UC / Single Minors       OTHER            Title 8  Apprehensions   \n",
       "58742  UC / Single Minors      RUSSIA            Title 8  Apprehensions   \n",
       "58743  UC / Single Minors   VENEZUELA            Title 8  Apprehensions   \n",
       "\n",
       "       Encounter Count  \n",
       "0                    3  \n",
       "1                    2  \n",
       "2                    6  \n",
       "3                   11  \n",
       "4                   40  \n",
       "...                ...  \n",
       "58739               27  \n",
       "58740               76  \n",
       "58741                4  \n",
       "58742                1  \n",
       "58743                3  \n",
       "\n",
       "[58744 rows x 11 columns]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Removed \"Month Grouping column\"\n",
    "\n",
    "encounters_aor_cleaned_df = encounters_aor_df.drop(columns=['Month Grouping'])\n",
    "encounters_aor_cleaned_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "86c235e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Fiscal Year</th>\n",
       "      <th>Month</th>\n",
       "      <th>Component</th>\n",
       "      <th>Land Border Region</th>\n",
       "      <th>Area of Responsibility</th>\n",
       "      <th>AOR</th>\n",
       "      <th>Demographic</th>\n",
       "      <th>Citizenship</th>\n",
       "      <th>Title of Authority</th>\n",
       "      <th>Encounter Type</th>\n",
       "      <th>Encounter Count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Inadmissibles</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>MEXICO</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Single Adults</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Single Adults</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Inadmissibles</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58739</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>GUATEMALA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58740</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>MEXICO</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58741</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58742</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>RUSSIA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58743</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>VENEZUELA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>58744 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Fiscal Year Month                   Component     Land Border Region  \\\n",
       "0            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "1            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "2            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "3            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "4            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "...           ...   ...                         ...                    ...   \n",
       "58739        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58740        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58741        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58742        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58743        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "\n",
       "      Area of Responsibility     AOR         Demographic Citizenship  \\\n",
       "0        Boston Field Office  Boston  Accompanied Minors      CANADA   \n",
       "1        Boston Field Office  Boston  Accompanied Minors      MEXICO   \n",
       "2        Boston Field Office  Boston  Accompanied Minors       OTHER   \n",
       "3        Boston Field Office  Boston       Single Adults      CANADA   \n",
       "4        Boston Field Office  Boston       Single Adults      CANADA   \n",
       "...                      ...     ...                 ...         ...   \n",
       "58739            Yuma Sector     YUM  UC / Single Minors   GUATEMALA   \n",
       "58740            Yuma Sector     YUM  UC / Single Minors      MEXICO   \n",
       "58741            Yuma Sector     YUM  UC / Single Minors       OTHER   \n",
       "58742            Yuma Sector     YUM  UC / Single Minors      RUSSIA   \n",
       "58743            Yuma Sector     YUM  UC / Single Minors   VENEZUELA   \n",
       "\n",
       "      Title of Authority Encounter Type  Encounter Count  \n",
       "0                Title 8  Inadmissibles                3  \n",
       "1               Title 42     Expulsions                2  \n",
       "2               Title 42     Expulsions                6  \n",
       "3               Title 42     Expulsions               11  \n",
       "4                Title 8  Inadmissibles               40  \n",
       "...                  ...            ...              ...  \n",
       "58739            Title 8  Apprehensions               27  \n",
       "58740            Title 8  Apprehensions               76  \n",
       "58741            Title 8  Apprehensions                4  \n",
       "58742            Title 8  Apprehensions                1  \n",
       "58743            Title 8  Apprehensions                3  \n",
       "\n",
       "[58744 rows x 11 columns]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Renamed Month (abbv) column to Month, and AOR (Abbv) to AOR.\n",
    "encounters_aor_cleaned_df.rename(columns={'Month (abbv)': 'Month', 'AOR (Abbv)': 'AOR'}, inplace=True)\n",
    "encounters_aor_cleaned_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f8705fc3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Fiscal Year</th>\n",
       "      <th>Month</th>\n",
       "      <th>Component</th>\n",
       "      <th>Land Border Region</th>\n",
       "      <th>Area of Responsibility</th>\n",
       "      <th>AOR</th>\n",
       "      <th>Demographic</th>\n",
       "      <th>Citizenship</th>\n",
       "      <th>Title of Authority</th>\n",
       "      <th>Encounter Type</th>\n",
       "      <th>Encounter Count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Inadmissibles</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>MEXICO</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Single Adults</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Single Adults</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Inadmissibles</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58739</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>GUATEMALA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58740</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>MEXICO</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58741</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58742</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>RUSSIA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58743</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>VENEZUELA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>58744 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Fiscal Year Month                   Component     Land Border Region  \\\n",
       "0            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "1            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "2            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "3            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "4            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "...           ...   ...                         ...                    ...   \n",
       "58739        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58740        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58741        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58742        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58743        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "\n",
       "      Area of Responsibility     AOR         Demographic Citizenship  \\\n",
       "0        Boston Field Office  Boston  Accompanied Minors      CANADA   \n",
       "1        Boston Field Office  Boston  Accompanied Minors      MEXICO   \n",
       "2        Boston Field Office  Boston  Accompanied Minors       OTHER   \n",
       "3        Boston Field Office  Boston       Single Adults      CANADA   \n",
       "4        Boston Field Office  Boston       Single Adults      CANADA   \n",
       "...                      ...     ...                 ...         ...   \n",
       "58739            Yuma Sector     YUM  UC / Single Minors   GUATEMALA   \n",
       "58740            Yuma Sector     YUM  UC / Single Minors      MEXICO   \n",
       "58741            Yuma Sector     YUM  UC / Single Minors       OTHER   \n",
       "58742            Yuma Sector     YUM  UC / Single Minors      RUSSIA   \n",
       "58743            Yuma Sector     YUM  UC / Single Minors   VENEZUELA   \n",
       "\n",
       "      Title of Authority Encounter Type  Encounter Count  \n",
       "0                Title 8  Inadmissibles                3  \n",
       "1               Title 42     Expulsions                2  \n",
       "2               Title 42     Expulsions                6  \n",
       "3               Title 42     Expulsions               11  \n",
       "4                Title 8  Inadmissibles               40  \n",
       "...                  ...            ...              ...  \n",
       "58739            Title 8  Apprehensions               27  \n",
       "58740            Title 8  Apprehensions               76  \n",
       "58741            Title 8  Apprehensions                4  \n",
       "58742            Title 8  Apprehensions                1  \n",
       "58743            Title 8  Apprehensions                3  \n",
       "\n",
       "[58744 rows x 11 columns]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Replaced China, Peoples Republic of with China in Citizenship column.\n",
    "encounters_aor_cleaned_df['Citizenship'] = encounters_aor_cleaned_df['Citizenship'].replace('CHINA, PEOPLES REPUBLIC OF', 'CHINA')\n",
    "encounters_aor_cleaned_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "dec47b99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Fiscal Year</th>\n",
       "      <th>Month</th>\n",
       "      <th>Component</th>\n",
       "      <th>Land Border Region</th>\n",
       "      <th>Area of Responsibility</th>\n",
       "      <th>AOR</th>\n",
       "      <th>Demographic</th>\n",
       "      <th>Citizenship</th>\n",
       "      <th>Title of Authority</th>\n",
       "      <th>Encounter Type</th>\n",
       "      <th>Encounter Count</th>\n",
       "      <th>Continent</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Inadmissibles</td>\n",
       "      <td>3</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>MEXICO</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>2</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>6</td>\n",
       "      <td>Unknown</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Single Adults</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>11</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Single Adults</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Inadmissibles</td>\n",
       "      <td>40</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58739</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>GUATEMALA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>27</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58740</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>MEXICO</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>76</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58741</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>4</td>\n",
       "      <td>Unknown</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58742</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>RUSSIA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>1</td>\n",
       "      <td>Europe</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58743</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>VENEZUELA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>3</td>\n",
       "      <td>South America</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>58744 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Fiscal Year Month                   Component     Land Border Region  \\\n",
       "0            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "1            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "2            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "3            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "4            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "...           ...   ...                         ...                    ...   \n",
       "58739        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58740        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58741        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58742        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58743        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "\n",
       "      Area of Responsibility     AOR         Demographic Citizenship  \\\n",
       "0        Boston Field Office  Boston  Accompanied Minors      CANADA   \n",
       "1        Boston Field Office  Boston  Accompanied Minors      MEXICO   \n",
       "2        Boston Field Office  Boston  Accompanied Minors       OTHER   \n",
       "3        Boston Field Office  Boston       Single Adults      CANADA   \n",
       "4        Boston Field Office  Boston       Single Adults      CANADA   \n",
       "...                      ...     ...                 ...         ...   \n",
       "58739            Yuma Sector     YUM  UC / Single Minors   GUATEMALA   \n",
       "58740            Yuma Sector     YUM  UC / Single Minors      MEXICO   \n",
       "58741            Yuma Sector     YUM  UC / Single Minors       OTHER   \n",
       "58742            Yuma Sector     YUM  UC / Single Minors      RUSSIA   \n",
       "58743            Yuma Sector     YUM  UC / Single Minors   VENEZUELA   \n",
       "\n",
       "      Title of Authority Encounter Type  Encounter Count      Continent  \n",
       "0                Title 8  Inadmissibles                3  North America  \n",
       "1               Title 42     Expulsions                2  North America  \n",
       "2               Title 42     Expulsions                6        Unknown  \n",
       "3               Title 42     Expulsions               11  North America  \n",
       "4                Title 8  Inadmissibles               40  North America  \n",
       "...                  ...            ...              ...            ...  \n",
       "58739            Title 8  Apprehensions               27  North America  \n",
       "58740            Title 8  Apprehensions               76  North America  \n",
       "58741            Title 8  Apprehensions                4        Unknown  \n",
       "58742            Title 8  Apprehensions                1         Europe  \n",
       "58743            Title 8  Apprehensions                3  South America  \n",
       "\n",
       "[58744 rows x 12 columns]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Created dictionary to add the Continent Column\n",
    "citizenship_to_continent = {\n",
    "    'BRAZIL': 'South America',\n",
    "    'CANADA': 'North America',\n",
    "    'CHINA': 'Asia',\n",
    "    'COLOMBIA': 'South America',\n",
    "    'CUBA': 'North America',\n",
    "    'ECUADOR': 'South America',\n",
    "    'EL SALVADOR': 'North America',\n",
    "    'GUATEMALA': 'North America',\n",
    "    'HAITI': 'North America',\n",
    "    'HONDURAS': 'North America',\n",
    "    'INDIA': 'Asia',\n",
    "    'MEXICO': 'North America',\n",
    "    'MYANMAR (BURMA)': 'Asia',\n",
    "    'NICARAGUA': 'North America',\n",
    "    'OTHER': 'Unknown',\n",
    "    'PERU': 'South America',\n",
    "    'PHILIPPINES': 'Asia',\n",
    "    'ROMANIA': 'Europe',\n",
    "    'RUSSIA': 'Europe',\n",
    "    'TURKEY': 'Asia', \n",
    "    'UKRAINE': 'Europe',\n",
    "    'VENEZUELA': 'South America'\n",
    "}\n",
    "\n",
    "encounters_aor_cleaned_df['Continent'] = encounters_aor_cleaned_df['Citizenship'].map(citizenship_to_continent).fillna('Unknown')\n",
    "encounters_aor_cleaned_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f61162ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Fiscal Year</th>\n",
       "      <th>Month</th>\n",
       "      <th>Component</th>\n",
       "      <th>Land Border Region</th>\n",
       "      <th>Area of Responsibility</th>\n",
       "      <th>AOR</th>\n",
       "      <th>Demographic</th>\n",
       "      <th>Citizenship</th>\n",
       "      <th>Title of Authority</th>\n",
       "      <th>Encounter Type</th>\n",
       "      <th>Encounter Count</th>\n",
       "      <th>Continent</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Inadmissibles</td>\n",
       "      <td>3</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>MEXICO</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>2</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>6</td>\n",
       "      <td>Unknown</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Single Adults</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>11</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Single Adults</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Inadmissibles</td>\n",
       "      <td>40</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58739</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>GUATEMALA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>27</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58740</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>MEXICO</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>76</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58741</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>4</td>\n",
       "      <td>Unknown</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58742</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>RUSSIA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>1</td>\n",
       "      <td>Europe</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58743</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>VENEZUELA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>3</td>\n",
       "      <td>South America</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>58744 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Fiscal Year Month                   Component     Land Border Region  \\\n",
       "0            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "1            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "2            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "3            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "4            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "...           ...   ...                         ...                    ...   \n",
       "58739        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58740        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58741        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58742        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58743        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "\n",
       "      Area of Responsibility     AOR         Demographic Citizenship  \\\n",
       "0        Boston Field Office  Boston  Accompanied Minors      CANADA   \n",
       "1        Boston Field Office  Boston  Accompanied Minors      MEXICO   \n",
       "2        Boston Field Office  Boston  Accompanied Minors       OTHER   \n",
       "3        Boston Field Office  Boston       Single Adults      CANADA   \n",
       "4        Boston Field Office  Boston       Single Adults      CANADA   \n",
       "...                      ...     ...                 ...         ...   \n",
       "58739            Yuma Sector     YUM  UC / Single Minors   GUATEMALA   \n",
       "58740            Yuma Sector     YUM  UC / Single Minors      MEXICO   \n",
       "58741            Yuma Sector     YUM  UC / Single Minors       OTHER   \n",
       "58742            Yuma Sector     YUM  UC / Single Minors      RUSSIA   \n",
       "58743            Yuma Sector     YUM  UC / Single Minors   VENEZUELA   \n",
       "\n",
       "      Title of Authority Encounter Type  Encounter Count      Continent  \n",
       "0                Title 8  Inadmissibles                3  North America  \n",
       "1               Title 42     Expulsions                2  North America  \n",
       "2               Title 42     Expulsions                6        Unknown  \n",
       "3               Title 42     Expulsions               11  North America  \n",
       "4                Title 8  Inadmissibles               40  North America  \n",
       "...                  ...            ...              ...            ...  \n",
       "58739            Title 8  Apprehensions               27  North America  \n",
       "58740            Title 8  Apprehensions               76  North America  \n",
       "58741            Title 8  Apprehensions                4        Unknown  \n",
       "58742            Title 8  Apprehensions                1         Europe  \n",
       "58743            Title 8  Apprehensions                3  South America  \n",
       "\n",
       "[58744 rows x 12 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Saved cleaned dataframe as encounters_aor_df\n",
    "\n",
    "encounters_aor_df = encounters_aor_cleaned_df\n",
    "encounters_aor_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "10b951f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exported encounters_df to a csv file located in a folder.\n",
    "\n",
    "encounters_aor_df.to_csv('.venv/encounters_aor_df.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2a571e2f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Office of Field Operations' 'U.S. Border Patrol']\n"
     ]
    }
   ],
   "source": [
    "# Unique Component\n",
    "unique_component = encounters_aor_df[\"Component\"].unique()\n",
    "print(unique_component)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c6470a72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Northern Land Border' 'Other' 'Southwest Land Border']\n"
     ]
    }
   ],
   "source": [
    "# Unique Land Border Regions\n",
    "unique_landborderregion = encounters_aor_df[\"Land Border Region\"].unique()\n",
    "print(unique_landborderregion)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "556fb0a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Boston Field Office' 'Buffalo Field Office' 'Detroit Field Office'\n",
      " 'Seattle Field Office' 'Atlanta Field Office' 'Baltimore Field Office'\n",
      " 'Chicago Field Office' 'Houston Field Office' 'Laredo Field Office'\n",
      " 'Los Angeles Field Office' 'Miami Field Office'\n",
      " 'New Orleans Field Office' 'New York Field Office'\n",
      " 'Portland Field Office' 'Preclearance Field Office'\n",
      " 'San Diego Field Office' 'San Francisco Field Office'\n",
      " 'San Juan Field Office' 'Tampa Field Office' 'Tucson Field Office'\n",
      " 'El Paso Field Office' 'Blaine Sector' 'Buffalo Sector' 'Detroit Sector'\n",
      " 'Grand Forks Sector' 'Havre Sector' 'Houlton Sector' 'Spokane Sector'\n",
      " 'Swanton Sector' 'Miami Sector' 'New Orleans Sector' 'Ramey Sector'\n",
      " 'Big Bend Sector' 'Del Rio Sector' 'El Centro Sector' 'El Paso Sector'\n",
      " 'Laredo Sector' 'Rio Grande Valley Sector' 'San Diego Sector'\n",
      " 'Tucson Sector' 'Yuma Sector']\n"
     ]
    }
   ],
   "source": [
    "# Unique Area of Responsibility\n",
    "unique_areaofresponsibility = encounters_aor_df[\"Area of Responsibility\"].unique()\n",
    "print(unique_areaofresponsibility)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a7267041",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Boston' 'Buffalo' 'Detroit' 'Seattle' 'Atlanta' 'Baltimore' 'Chicago'\n",
      " 'Houston' 'Laredo' 'Los Angeles' 'Miami' 'New Orleans' 'New York'\n",
      " 'Portland' 'Preclearance' 'San Diego' 'San Francisco' 'San Juan' 'Tampa'\n",
      " 'Tucson' 'El Paso' 'BLW' 'BUN' 'DTM' 'GFN' 'HVM' 'HLT' 'SPW' 'SWB' 'MIP'\n",
      " 'NLL' 'RMY' 'BBT' 'DRT' 'ELC' 'EPT' 'LRT' 'RGV' 'SDC' 'TCA' 'YUM']\n"
     ]
    }
   ],
   "source": [
    "# Unique AOR\n",
    "unique_aor = encounters_aor_df[\"AOR\"].unique()\n",
    "print(unique_aor)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "1921341e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['CANADA' 'MEXICO' 'OTHER' 'CHINA' 'COLOMBIA' 'INDIA' 'RUSSIA' 'VENEZUELA'\n",
      " 'UKRAINE' 'EL SALVADOR' 'CUBA' 'ECUADOR' 'GUATEMALA' 'HAITI'\n",
      " 'PHILIPPINES' 'TURKEY' 'HONDURAS' 'NICARAGUA' 'ROMANIA' 'BRAZIL'\n",
      " 'MYANMAR (BURMA)' 'PERU']\n"
     ]
    }
   ],
   "source": [
    "# Unique Citizenships\n",
    "unique_citizenship = encounters_aor_df[\"Citizenship\"].unique()\n",
    "print(unique_citizenship)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "94eafa0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Accompanied Minors' 'Single Adults' 'FMUA' 'UC / Single Minors']\n"
     ]
    }
   ],
   "source": [
    "# Unique Demographic\n",
    "\n",
    "unique_demographic = encounters_aor_df[\"Demographic\"].unique()\n",
    "print(unique_demographic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "9c9ac6ab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Title 8' 'Title 42']\n"
     ]
    }
   ],
   "source": [
    "# Unique Title of Authority\n",
    "unique_titleofauthority = encounters_aor_df[\"Title of Authority\"].unique()\n",
    "print(unique_titleofauthority)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4708d64e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Inadmissibles' 'Expulsions' 'Apprehensions']\n"
     ]
    }
   ],
   "source": [
    "# Unique Encounter Type\n",
    "unique_encountertype = encounters_aor_df[\"Encounter Type\"].unique()\n",
    "print(unique_encountertype)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "eacc4a82",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2021 2022 2023 2024]\n"
     ]
    }
   ],
   "source": [
    "unique_fiscalyear = encounters_aor_df[\"Fiscal Year\"].unique()\n",
    "print(unique_fiscalyear)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "efbef0cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['APR' 'AUG' 'DEC' 'FEB' 'JAN' 'JUL' 'JUN' 'MAR' 'MAY' 'NOV' 'OCT' 'SEP']\n"
     ]
    }
   ],
   "source": [
    "unique_month = encounters_aor_df[\"Month\"].unique()\n",
    "print(unique_month)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "2ddce4a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 58744 entries, 0 to 58743\n",
      "Data columns (total 12 columns):\n",
      " #   Column                  Non-Null Count  Dtype \n",
      "---  ------                  --------------  ----- \n",
      " 0   Fiscal Year             58744 non-null  object\n",
      " 1   Month                   58744 non-null  object\n",
      " 2   Component               58744 non-null  object\n",
      " 3   Land Border Region      58744 non-null  object\n",
      " 4   Area of Responsibility  58744 non-null  object\n",
      " 5   AOR                     58744 non-null  object\n",
      " 6   Demographic             58744 non-null  object\n",
      " 7   Citizenship             58744 non-null  object\n",
      " 8   Title of Authority      58744 non-null  object\n",
      " 9   Encounter Type          58744 non-null  object\n",
      " 10  Encounter Count         58744 non-null  int64 \n",
      " 11  Continent               58744 non-null  object\n",
      "dtypes: int64(1), object(11)\n",
      "memory usage: 5.4+ MB\n"
     ]
    }
   ],
   "source": [
    "encounters_aor_df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "93df5169",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Fiscal Year</th>\n",
       "      <th>Month</th>\n",
       "      <th>Component</th>\n",
       "      <th>Land Border Region</th>\n",
       "      <th>Area of Responsibility</th>\n",
       "      <th>AOR</th>\n",
       "      <th>Demographic</th>\n",
       "      <th>Citizenship</th>\n",
       "      <th>Title of Authority</th>\n",
       "      <th>Encounter Type</th>\n",
       "      <th>Encounter Count</th>\n",
       "      <th>Continent</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Inadmissibles</td>\n",
       "      <td>3</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>MEXICO</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>2</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Accompanied Minors</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>6</td>\n",
       "      <td>Unknown</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Single Adults</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 42</td>\n",
       "      <td>Expulsions</td>\n",
       "      <td>11</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021</td>\n",
       "      <td>APR</td>\n",
       "      <td>Office of Field Operations</td>\n",
       "      <td>Northern Land Border</td>\n",
       "      <td>Boston Field Office</td>\n",
       "      <td>Boston</td>\n",
       "      <td>Single Adults</td>\n",
       "      <td>CANADA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Inadmissibles</td>\n",
       "      <td>40</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58739</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>GUATEMALA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>27</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58740</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>MEXICO</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>76</td>\n",
       "      <td>North America</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58741</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>4</td>\n",
       "      <td>Unknown</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58742</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>RUSSIA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>1</td>\n",
       "      <td>Europe</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58743</th>\n",
       "      <td>2024</td>\n",
       "      <td>SEP</td>\n",
       "      <td>U.S. Border Patrol</td>\n",
       "      <td>Southwest Land Border</td>\n",
       "      <td>Yuma Sector</td>\n",
       "      <td>YUM</td>\n",
       "      <td>UC / Single Minors</td>\n",
       "      <td>VENEZUELA</td>\n",
       "      <td>Title 8</td>\n",
       "      <td>Apprehensions</td>\n",
       "      <td>3</td>\n",
       "      <td>South America</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>58744 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Fiscal Year Month                   Component     Land Border Region  \\\n",
       "0            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "1            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "2            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "3            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "4            2021   APR  Office of Field Operations   Northern Land Border   \n",
       "...           ...   ...                         ...                    ...   \n",
       "58739        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58740        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58741        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58742        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "58743        2024   SEP          U.S. Border Patrol  Southwest Land Border   \n",
       "\n",
       "      Area of Responsibility     AOR         Demographic Citizenship  \\\n",
       "0        Boston Field Office  Boston  Accompanied Minors      CANADA   \n",
       "1        Boston Field Office  Boston  Accompanied Minors      MEXICO   \n",
       "2        Boston Field Office  Boston  Accompanied Minors       OTHER   \n",
       "3        Boston Field Office  Boston       Single Adults      CANADA   \n",
       "4        Boston Field Office  Boston       Single Adults      CANADA   \n",
       "...                      ...     ...                 ...         ...   \n",
       "58739            Yuma Sector     YUM  UC / Single Minors   GUATEMALA   \n",
       "58740            Yuma Sector     YUM  UC / Single Minors      MEXICO   \n",
       "58741            Yuma Sector     YUM  UC / Single Minors       OTHER   \n",
       "58742            Yuma Sector     YUM  UC / Single Minors      RUSSIA   \n",
       "58743            Yuma Sector     YUM  UC / Single Minors   VENEZUELA   \n",
       "\n",
       "      Title of Authority Encounter Type  Encounter Count      Continent  \n",
       "0                Title 8  Inadmissibles                3  North America  \n",
       "1               Title 42     Expulsions                2  North America  \n",
       "2               Title 42     Expulsions                6        Unknown  \n",
       "3               Title 42     Expulsions               11  North America  \n",
       "4                Title 8  Inadmissibles               40  North America  \n",
       "...                  ...            ...              ...            ...  \n",
       "58739            Title 8  Apprehensions               27  North America  \n",
       "58740            Title 8  Apprehensions               76  North America  \n",
       "58741            Title 8  Apprehensions                4        Unknown  \n",
       "58742            Title 8  Apprehensions                1         Europe  \n",
       "58743            Title 8  Apprehensions                3  South America  \n",
       "\n",
       "[58744 rows x 12 columns]"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "encounters_aor_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "3ed3deb1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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BeCSSy7hpJNOAuDwww/njjvuYPHixSxevJg77riDww8/vNnjzZgxg3HjxjXb5owzzuCll15i3rx53H///fTr168hHM+cOZPTTjuN6dOns8suu2zoy253DMiSJEmbyO9+9zuuv/567rrrLgYPHszgwYO59dZbmTt3LjvttBMAd999N/vssw/9+vXj1Vdf5dxzzwWge/funHfeeQwdOpShQ4cyceJEunfvDsCVV15J7969WbBgAQMHDuSzn/0sAC+88AJdu3ZtOH6fPn0466yzmDp1Kr17915jBY3Gxo8fz7Jlyzj22GMZPHgwRx11VDXels1ONDXfpS2rq6vL+vr6WpchSe1a3ZTzal2C2pj60y+qdQmbtTFjxjBt2jS23nrrTdrv+PHjOfHEExk4cOAm7XdLERGPZGZd4+3OQZYkSZuFC+89qdYlbLChE3bhkgdPX3fD9dTtSLjlz5dzy72bvOs27/zDrq1a306xkCRJkkoMyJIkSVKJAVmSJEkqMSBLkiRJJQZkSS02f/58RowYQf/+/dl333254oor1mjzhS98oWFpo379+rHDDjs07HvhhRf40Ic+RP/+/RkwYEDDNzplJueeey79+vWjf//+XHnllWv0O2/ePLp27drQ9+mn//1ilxtvvJH999+fgQMHcsQRR7Bo0SIAJk2axIABAxg4cCAjR47k+eef37RviCSpXXIVC0kt1rFjRy677DIOOOAAli5dyoEHHsioUaMYMGBAQ5tvfetbDfe//e1vM3PmzIbH48aN49xzz2XUqFEsW7aMrbaq/I0+depU5s+fz9y5c9lqq6147bXXmjz+XnvtxaxZs1bbtmLFCj73uc8xZ84cdt55ZyZMmMDkyZO54IILGDJkCPX19WyzzTZcddVVTJgwgZtuumkTviOSpPbIEWRJLdazZ08OOOAAALbddlv69+/Piy++uNb2N954I8cffzwAc+bMYcWKFYwaNQqAbt26sc022wBw1VVXMXHixIbAvD7f5pSZZCZ//etfyUyWLFlCr169ABgxYkTDMYYNG8aCBQvW8xVLkrZEBmRJG2TevHnMnDmTgw8+uMn9zz//PM899xwf/OAHAXjyySfZYYcd+PjHP86QIUMYP348K1euBOCZZ57hpptuoq6ujtGjR/PUU0812edzzz3HkCFD+MAHPsB9990HQKdOnbjqqqvYf//9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PSIGNGozGuhb3E4Frmpx5VuAww47jO7du691/5w5cxg5ciQAI0aM4Oc///k6+7zqqquYOHEiW21V+dHvsssu61XTsGHD6Nmz5yapRZIkqS1qNiBHxFbAL4BDgLrMXA68CXx0XR1n5suZ+WhxfynwOLBro2YfBX6YFQ8CO0TEmulLTRo0aBA333wzALfccgtLly7l9ddfB+Dtt9+mrq6OYcOG8bOf/azhOc888ww33XQTdXV1jB49mqeeeqrJvp977jmGDBnCBz7wAe67776NqkWSJGlz0mxAzsx3gcsyc3Fmriy2/TUzX1mfg0REH2AI8FCjXbsC80uPF7BmiCYiTo2I+oioX7hw4focul279NJLueeeexgyZAj33HMPu+66Kx07dgTghRdeoL6+nh//+Md8/vOf55lnngHgnXfeoUuXLtTX13PKKadw0kknrdFvz549eeGFF5g5cyaTJk3ik5/8JEuWLNngWiRJkjYnLZlicUdEjI2I2JADREQ34Gbg88XFfqvtbuIpucaGzKszsy4z63r06LEhZbRLvXr1Ytq0acycOZOLL74YgO23375hH8Cee+7J8OHDmTlzJgC9e/dm7NixABx99NHMnj17jX47d+7MTjvtBMCBBx7IXnvtxZNPPrnBtUiSJG1OWhKQzwL+B/hbRCyJiKUR0fxwYiEiOlEJxz/KzGlNNFkA7FZ63Bt4qSV9b6kmT57M5MmTAVi0aBHvvvsuAJdccknDaPDixYt55513Gtr87ne/Y8CAyvTvj33sY9x1110A3HPPPfTr1w+AGTNmMG7cOAAWLlzIypUrAXj22Wd56qmn2HPPPZuta221SJIkbW7WGZAzc9vM3CozO2XmdsXj7db1vGLE+Rrg8cyctJZm04FxxWoWw4C/ZObL6/UK2rHjjz+eQw45hCeeeILevXtzzTXXMHfu3IbR3bvvvpt99tmHfv368eqrr3LuuecC8Pjjj1NXV8egQYMYMWIEZ599dkNAPvvss7n55pvZf//9Oeecc/jBD34AVKZkdO3aFYB7772XgQMHMmjQII455himTJnScLHghAkT6N27N2+++Sa9e/fmggsuaLYWSZKkzU1krjGjYfUGlaB7AvCPmXlRROwG9MzMNdf6Wv15hwL3AX8A3i02fxnYHSAzpxR9TwaOoHLx32cys765fuvq6rK+vtkm7dqYMWOY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",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 1. Sum of Encounters by Fiscal Year. Use a bar plot to visualize the data. Add title and labels. Add results to top of each bar.\n",
    "encounters_by_fiscal_year = encounters_aor_df.groupby('Fiscal Year')['Encounter Count'].sum().reset_index()\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.barplot(data=encounters_by_fiscal_year, x='Fiscal Year', y='Encounter Count', palette='viridis')\n",
    "plt.title('Total Encounters by Fiscal Year')\n",
    "plt.xlabel('Fiscal Year')\n",
    "plt.ylabel('Total Encounters')\n",
    "for index, row in encounters_by_fiscal_year.iterrows():\n",
    "    plt.text(index, row['Encounter Count'], f\"{row['Encounter Count']:,}\", color='black', ha='center', va='bottom')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "50a408cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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WrPDkCRJkiSt5iLi0Y7KHeIuSZIkSVIFmKBLkiRJklQBJuiSJEmSJFWAc9BXYNGiRcyePZv58+c3O5Ru07dvX7bYYgvWXHPNZociSZIkSS3FBH0FZs+eTb9+/Rg0aBAR0exwGi4zef7555k9ezaDBw9udjiSJEmS1FIc4r4C8+fPZ6ONNmqJ5BwgIthoo41aasSAJEmSJFWFCfpKtEpy3qbVnq8kSZIkVYUJuiRJkiRJFWCCvgrWWGMNhg8fvvRn1qxZvOc97+my/d9yyy3st99+y5Q988wzDB48mKeeempp2XHHHcfEiRO77HElSZIkSc3jInGrYO211+a+++5bpuwPf/hDQx9z00035eSTT+Zzn/scP/7xj7nnnnu47bbbuPvuu1d5n4sXL6Z3b18CkiRJklQF9qB3kXXXXReAOXPmsNtuuzF8+HC22247/vd//xeA//mf/2GHHXZg++23Z9SoUQDcddddvOc972HEiBG85z3v4S9/+csKH2PcuHH89a9/5be//S3HH3885513Ho899hj77LMPO+64I7vuuisPPfQQANdeey0777wzI0aM4H3vex9PP/00ABMmTGDcuHHstddeHHPMMY1qDkmSJElSJ9l9ugr++c9/Mnz4cAAGDx7ML3/5y6X3/fSnP2Xvvffmi1/8IkuWLOGVV17h2Wef5ROf+AS33norgwcPZu7cuQBss8023HrrrfTu3Zvf/OY3fOELX+DKK69c7uP26tWLCy64gD333JPRo0ez2267MWrUKL7//e+z9dZbc+edd3Lcccdx88038973vpc77riDiOC///u/+frXv84555wDwN13381tt93G2muv3bhGkiRJkiR1ign6KuhoiHubd77znXzsYx9j0aJFfOhDH2L48OHccsst7LbbbkuvLb7hhhsC8NJLLzFmzBgefvhhIoJFixat9LHbeuaPO+445s2bxx/+8AcOPfTQpfcvWLAAKK7hfvjhhzNnzhwWLly4zHXNR48ebXIuSZIkSRXjEPcutttuu3Hrrbey+eabc/TRR3PJJZeQmR1evuxLX/oSe+yxB/fffz/XXntt3dcf79WrF7169eLVV19lgw024L777lv6M2PGDABOOOEEjj/+eKZPn86FF164zL7f9KY3dc2TlSRJkiR1GRP0Lvboo4+y6aab8olPfIKxY8dyzz338O53v5vf/e53PPLIIwBLh7i/9NJLbL755gD86Ec/6vRjrbfeegwePJjLL78cgMzkT3/60+v2PXny5Df6tCRJkiRJDWaC3sVuueUWhg8fzogRI7jyyis58cQT2WSTTbjooos46KCD2H777Tn88MMB+PznP88pp5zCLrvswpIlS1bp8X7yk58wadIktt9+e4YOHcrVV18NFIvBHXrooey6665svPHGXfb8JEmSJEmNEZnZ7BgqYeTIkTlt2rRlymbMmMGQIUOaFFHztOrzliRJkqTuEBF3Z+bI9uX2oEuSJEmSVAEm6JIkSZIkVYCXWZPUKTO2qW/6w5CHZjQ4EkmSJGn1Yg+6JEmSJEkVYIIuSZIkSVIFmKBLkiRJklQBzkHvhEHjf9Wl+5s1cd+V1nn88cc55phjeOqpp+jVqxfjxo3jxBNPZO7cuRx++OHMmjWLQYMGMWXKFPr378/UqVMZP348CxcupE+fPpx99tnsueeeAHzxi1/kkksu4YUXXmDevHld+lwkSZIkSW+MPegV17t3b8455xxmzJjBHXfcwfnnn8+DDz7IxIkTGTVqFA8//DCjRo1i4sSJAGy88cZce+21TJ8+ncmTJ3P00Ucv3df+++/PXXfd1aynIkmSJElaARP0ihs4cCA77LADAP369WPIkCE88cQTXH311YwZMwaAMWPGcNVVVwEwYsQINttsMwCGDh3K/PnzWbBgAQDvete7GDhwYPc/CUmSJEnSSpmg9yCzZs3i3nvvZeedd+bpp59emmwPHDiQZ5555nX1r7zySkaMGMFaa63V3aFKkiRJkjrJOeg9xLx58zj44IM599xzWW+99VZa/4EHHuDkk0/mxhtv7IboJEmSJElvlD3oPcCiRYs4+OCDOeqoozjooIMAGDBgAHPmzAFgzpw5bLrppkvrz549mwMPPJBLLrmErbbaqikxS5IkSZI6xwS94jKTsWPHMmTIEE466aSl5aNHj2by5MkATJ48mQMOOACAF198kX333ZezzjqLXXbZpSkxS5IkSZI6zyHunVDPZdG62u9//3suvfRShg0bxvDhwwE488wzGT9+PIcddhiTJk1iyy235PLLLwfgvPPOY+bMmZx++umcfvrpANx4441suummfP7zn+enP/0pr7zyCltssQUf//jHmTBhQrc/J0mSJEnS60VmNjuGShg5cmROmzZtmbIZM2Yw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AGC99dYDYPHixSxcuJCI6OZnI0mSJElaHhP0HmTWrFnce++97Lzzzjz99NMMHDgQKJL4Z5555nX1r7zySkaMGMFaa621tGzvvfdm0003pV+/fhxyyCHdFrskSZIkacVM0HuIefPmcfDBB3Puuecu7QlfkQceeICTTz6ZCy+8cJnyX//618yZM4cFCxZw8803NypcSZIkSVInmaD3AIsWLeLggw/mqKOO4qCDDgJgwIABzJkzB4A5c+aw6aabLq0/e/ZsDjzwQC655BK22mqr1+2vb9++jB49mquvvrp7noAkSZIkaaVM0CsuMxk7dixDhgzhpJNOWlo+evRoJk+eDMDkyZM54IADAHjxxRfZd999Oeuss9hll12W1p83b97ShH7x4sVcf/31bLPNNt34TCRJkiRJK+Jl1jqhGRew//3vf8+ll17KsGHDGD58OABnnnkm48eP57DDDmPSpElsueWWS1dkP++885g5cyann346p59+OgA33ngjmcno0aNZsGABS5YsYc899+RTn/pUtz8fSZIkSVLHTNAr7r3vfS+Z2eF9N9100+vKTj31VE499dQO6//xj3/s0tgkSZIkSV3HIe6SJEmSJFWACbokSZIkSRVggi5JkiRJUgWYoEuSJEmSVAEm6JIkSZIkVYAJuiRJkiRJFeBl1jphxjZDunR/Qx6asdI6jz/+OMcccwxPPfUUvXr1Yty4cZx44onMnTuXww8/nFmzZjFo0CCmTJlC//79mTp1KuPHj2fhwoX06dOHs88+mz333HOZfY4ePZq//e1v3H///V36fCRJkiRJq84e9Irr3bs355xzDjNmzOCOO+7g/PPP58EHH2TixImMGjWKhx9+mFGjRjFx4kQANt54Y6699lqmT5/O5MmTOfroo5fZ3y9+8QvWXXfdZjwVSZIkSdIKmKBX3MCBA9lhhx0A6NevH0OGDOGJJ57g6quvZsyYMQCMGTOGq666CoARI0aw2WabATB06FDmz5/PggULAJg3bx7f/OY3OfXUU7v/iUiSJEmSVsgEvQeZNWsW9957LzvvvDNPP/00AwcOBIok/plnnnld/SuvvJIRI0aw1lprAfClL32Jz372s6yzzjrdGrckSZIkaeVM0HuIefPmcfDBB3Puueey3nrrrbT+Aw88wMknn8yFF14IwH333cfMmTM58MADGx2qJEmSJGkV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",
      "text/plain": [
       "<Figure size 1008x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Month           APR     AUG     DEC     FEB     JAN     JUL     JUN     MAR  \\\n",
      "Fiscal Year                                                                   \n",
      "2021         196190  231243   92746  115559   95276  233919  207823  192025   \n",
      "2022         262109  251521  205691  190578  186808  238929  247523  250404   \n",
      "2023         276036  304073  302392  213911  209151  245154  211457  259471   \n",
      "2024         247929  158893  370883  256071  242530  170180  204932  246505   \n",
      "\n",
      "Month           MAY     NOV     OCT     SEP  \n",
      "Fiscal Year                                  \n",
      "2021         198459   89072   90585  213622  \n",
      "2022         274992  198553  187136  272338  \n",
      "2023         275166  284624  278317  341392  \n",
      "2024         240924  308605  309024  144666  \n"
     ]
    }
   ],
   "source": [
    "# 2. Group by Fiscal Year and Month, then sum Encounter Count\n",
    "encounters_by_year_month = encounters_aor_df.groupby(['Fiscal Year', 'Month'])['Encounter Count'].sum().unstack(fill_value=0)\n",
    "\n",
    "# Plot as a grouped bar chart\n",
    "encounters_by_year_month.T.plot(kind='bar', figsize=(14, 7))\n",
    "plt.title('Total Encounters by Fiscal Year and Month')\n",
    "plt.xlabel('Month')\n",
    "plt.ylabel('Encounter Count')\n",
    "plt.xticks(rotation=45)\n",
    "plt.legend(title='Fiscal Year')\n",
    "plt.tight_layout()\n",
    "plt.grid(axis='y')\n",
    "plt.show()\n",
    "\n",
    "print(encounters_by_year_month)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "9d99f9bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Month           APR     AUG     DEC     FEB     JAN     JUL     JUN     MAR  \\\n",
      "Fiscal Year                                                                   \n",
      "2021         196190  231243   92746  115559   95276  233919  207823  192025   \n",
      "2022         262109  251521  205691  190578  186808  238929  247523  250404   \n",
      "2023         276036  304073  302392  213911  209151  245154  211457  259471   \n",
      "2024         247929  158893  370883  256071  242530  170180  204932  246505   \n",
      "\n",
      "Month           MAY     NOV     OCT     SEP  \n",
      "Fiscal Year                                  \n",
      "2021         198459   89072   90585  213622  \n",
      "2022         274992  198553  187136  272338  \n",
      "2023         275166  284624  278317  341392  \n",
      "2024         240924  308605  309024  144666  \n"
     ]
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 864x432 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "print(encounters_by_year_month)\n",
    "# Visualize the data. Add table. No heatmap.\n",
    "plt.figure(figsize=(12, 6))\n",
    "sns.heatmap(encounters_by_year_month, annot=True, fmt='d', cmap='viridis', cbar_kws={'label': 'Encounter Count'})\n",
    "plt.title('Total Encounters by Fiscal Year and Month')\n",
    "plt.xlabel('Fiscal Year')\n",
    "plt.ylabel('Month')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "plt.show()  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "45449912",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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SZKkJUJEjMnMQXMvb60e5P2AG5t6ICKOiojRETF68uTJrVTO4pkyZQp///vfOfzwwwHo3LnzPKOyEcGUKVMAePvttxsDcOfOnVl22WUBmDZtGrNmzXv11nfeeYd77rmnyRHkiGDq1KnMmDGD999/n86dO9O1a1cyk8xk6tSpZCZTpkyZJ3RDMcq8//77L86vL0mStFSreUCOiM7AbsBvm3o8M6/IzEGZOah793nmaW6TXnjhBbp3786wYcMYOHAgRxxxBFOnTp1jndNOO43rrruOnj17MnjwYC666KLGxyZMmEC/fv1Ye+21Ofnkk+cJsjfffDM77rgjXbt2nWffe++9NyussAJrrrkm66yzDieccAKrrbYayyyzDJdeeimbbLJJ40jy7AA/24svvsi4cePYYYcdWvDVkCRJWrq0xgjyrsAjmflqK+yrVcyYMYNHHnmEo48+mkcffZQVVliBn/zkJ3Osc+ONN3LooYcyceJEbr/9dg466KDG0eK1116bxx9/nOeee45rrrmGV199dZ7nzm+Ud9SoUXTs2JFJkyYxbtw4zjvvPF544QU+/PBDLr30Uh599FEmTZpEv3795uhPBhgxYgR77703HTt2bMFXQ5IkaenSGgF5f+bTXrGk6tmzJz179mTLLbcEilHdRx55ZI51rrzySoYOHQrAVlttxQcffNB40txsPXr0YKONNuK+++5rXPbGG28watQovvjFLza57xtuuIFddtmFZZZZhjXWWIOtt96a0aNH09DQAMB6661HRDB06FAefPDBOZ47YsQI2yskSZIWoqYBOSKWB74A/L6W+2ltH//4x1l77bV5+umnARg5ciR9+/bl4osv5uKLLwZgnXXWYeTIkQA8+eSTfPDBB3Tv3p2JEyfy/vvvA/Dmm2/ywAMPsMEGGzRu+7e//S1DhgxhueWWa1w2atSoxpP11llnHe65557GfuOHH36YDTfckLXWWouxY8cyu4/77rvvpk+fPo3bePrpp3nzzTfZaqutavjKSJIkLfk61XLjmfkesHot91EvF110EQceeCDTp09n3XXX5Ve/+hWnnnoqW29dTNRx3nnnceSRR3L++ecTEVx99dVEBE8++STHH388EUFmcsIJJ7DJJps0bnfEiBGccsopc+zrpZdeokuXLgB84xvfYNiwYWy88cZkJsOGDaNfv34AfP/732fb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A8WI88orr8wbb7wBwAcffMCgQYP49Kc/3RiC33jjDVZZZRU6deoEQM+ePecJ3QD9+/fn1ltvZcaMGYwbN44xY8YwYcIEAE499VSOP/54ll9++Tmec9ppp3HdddfRs2dPBg8ezEUXXdSir4EkSUsqA7LUwt5991322msvLrjgArp27TrHY02NFkcEUPQEjx49mhtuuIFjjz2W559/foHrVx122GH07NmTQYMGceyxx/KZz3yGTp060dDQwHPPPceee+45z3NuvPFGDj30UCZOnMjtt9/OQQcdNEdbhiRJ7ZUBWWpBH374IXvttRcHHnggX/7yl+d5vGfPno0juzNmzODtt99mtdVWA2hscVh33XXZbrvtePTRR+nWrRtvvfUWM2bMAGDixIlNtkJ06tSJ888/n4aGBm699Vbeeust1l9/fR566CHGjBlDr169+OxnP8szzzzDdtttBxT90EOHDgVgq6224oMPPuD1119v8ddEkqQljQFZaiGZyeGHH06fPn047rjjGpdffPHFXHzxxUAxk8Q111wDwE033cQOO+xARPDmm28ybdo0AF5//XUeeOAB+vbtS0Sw/fbbc9NNNwFwzTXXsPvuuwMwatQoDj74YADee+89pk6dCsDdd99Np06d6Nu3L0cffTSTJk1i/Pjx3H///XzqU59qnOFinXXWYeTIkQA8+eSTfPDBB3Tv3r3Gr5IkSW1fp3oXIC0tHnjgAa699lo22WQTBgwYAMAZZ5zBU089xdZbbw3A4YcfzkEHHUTv3r1ZbbXVGDFiBFAE1K9+9at06NCBWbNmccopp9C3b18AzjrrLPbbbz++973vMXDgQA4//HCgaMno0qULAK+99ho777wzHTp0YK211uLaa69daL3nnXceRx55JOeffz4RwdVXX91k+4YkSe1NLOgM+sXacMTawK+BjwOzgCsyc96JYSsGDRqUs8+8b64hO37nI9eo1vXHkWfUu4S6GDJkCL///e/p3Llzi273xBNP5KCDDqJfv34tul1JktqLiBiTmYPmXl7LEeQZwPGZ+UhErASMiYi7M3Pswp4oLa5tvvqjepfwf9bakh2/eVYNNtyVhy+5Fbi1BttuXfddfmq9S5AkqVHNepAz8z+Z+Uh5+x3gSWCtWu1PkiRJagmtcpJeRPQCBgL/aOKxoyJidESMnjx5cmuUI0mSJM1XzQNyRKwI/A44NjOnzP14Zl6RmYMyc5Bn0EuSJKneahqQI2IZinB8fWb+vpb7kiRJklpCzQJyFPNFXQk8mZk/rdV+JEmSpJZUyxHkrYGDgB0ioqH8GVzD/UmSJEmLrWbTvGXm/YBXHZAkSdISxUtNS5IkSRUGZEmSJKnCgCxJkiRVGJAlSZKkCgOyJEmSVGFAliRJkioMyJIkSVKFAVmSJEmqMCBLkiRJFQZkSZIkqcKALEmSJFUYkCVJkqQKA7IkSZJUYUCWJEmSKgzIkiRJUoUBWZIkSaowIEuSJEkVBmRJkiSpwoAsSZIkVRiQJUmSpAoDsiRJklRhQJYkSZIqDMiSJElShQFZkiRJqjAgS5IkSRUGZEmSJKnCgCxJkiRVGJAlSZKkCgOyJEmSVGFAliRJkioMyJIkSVKFAVmSJEmqMCBLkiRJFQZkSZIkqcKALEmSJFXULCBHxFUR8VpE/LtW+5AkSZJaWi1HkK8Gdqnh9iVJkqQWV7OAnJl/B/5bq+1LkiRJtVD3HuSIOCoiRkfE6MmTJ9e7HEmSJLVzdQ/ImXlFZg7KzEHdu3evdzmSVHNPP/00AwYMaPzp2rUrF1xwAQAXXXQRG2ywARtttBEnnXQSAG+88Qbbb789K664Isccc8x8tzty5Eg23XRTBgwYwGc/+1mee+45AG699Vb69evHgAEDGDRoEPfff3/jc3r16sUmm2zS+JgkqQ0EZElqbzbYYAMaGhpoaGhgzJgxLL/88uy555789a9/5dZbb+Xxxx/niSee4IQTTgBgueWW40c/+hHnnnvuArd79NFHc/3119PQ0MABBxzA6aefDsCOO+7IY489RkNDA1dddRVHHHHEHM/761//SkNDA6NHj67NL6xmWdAXJ4Bzzz2XiOD1119vXHbmmWfSu3dvNthgA/785z83ud2LL76Y3r17z/NcgHvvvZcBAwaw0UYb8bnPfa5ZdUjtQad6FyBJ7dnIkSNZb731+MQnPsGJJ57IKaecwrLLLgvAGmusAcAKK6wwx4jw/EQEU6ZMAeDtt9+mR48eAKy44oqN60ydOpWIqMWvosU0+4sTwMyZM1lrrbXYc889AZgwYQJ3330366yzTuP6Y8eOZcSIETzxxBNMmjSJz3/+8zzzzDN07Nhxju1uvfXWDBkyhO22226O5W+99RZf//rXufPOO1lnnXV47bXXFlqH1F7Ucpq3G4GHgA0iYmJEHF6rfUnSkmrEiBHsv//+ADzzzDPcd999bLnllnzuc5/jn//85yJt65e//CWDBw+mZ8+eXHvttZxyyimNj918881suOGGfPGLX+Sqq65qXB4R7LTTTmy22WZcccUVLfNLabFVvzgBDB8+nLPPPnuOLze33nor++23H8suuyyf/OQn6d27N6NGjZpnWwMHDqRXr17zLL/hhhv48pe/3Bi6Z38hW1AdUntRy1ks9s/MNTNzmczsmZlX1mpfkrQkmj59Orfddhv77LMPADNmzODNN9/k4Ycf5pxzzmHo0KFkZrO3d/7553P77bczceJEhg0bxnHHHdf42J577slTTz3FLbfcwqmnntq4/IEHHuCRRx7hjjvu4JJLLuHvf/97y/2C+siqX5xuu+021lprLfr37z/HOi+//DJrr7124/2ePXvy8ssvN3sfzzzzDG+++Sbbbbcdm222Gb/+9a8XWIfUntiDLEl1cscdd7DpppvysY99DCgCzpe//GUigi222IIOHTrM0zM6P5MnT+axxx5jyy23BGDfffflwQcfnGe9bbfdlueff75xu7PbMNZYYw323HPPJkcg1bqqX5zee+89fvzjH/PDH/5wnvWa+vK0KO0zM2bMYMyYMfzpT3/iz3/+Mz/60Y945plnmqxDam8MyJJUJzfeeOMco3N77LEH99xzD1CM7k2fPp1u3botcBsHH3wwo0aNYtVVV+Xtt99uDDh33303ffr0AeC5555rDFOPPPII06dPZ/XVV2fq1Km88847QNGbfNddd7Hxxhu3+O+pRVP94vT8888zbtw4+vfvT69evZg4cSKbbropr7zyCj179mTChAmNz5s4cWLjF57m6NmzJ7vssgsrrLAC3bp1Y9ttt+Wxxx5rsg6pvfEkPUmqg/fee4+7776byy+/vHHZYYcdxmGHHcbGG29M586dueaaaxpHBHv16sWUKVOYPn06t9xyC3fddRd9+/bl8ccfZ80116RTp0784he/YK+99qJDhw6suuqqjb3Gv/vd7/j1r3/NMsssQ5cuXfjNb35DRPDqq682nnw1Y8YMDjjgAHbZxQug1lv1i9Mmm2zSePIcFJ+D0aNH061bN3bbbTcOOOAAjjvuOCZNmsSzzz7LFltsARRfnI455pjG+03ZfffdOeaYY5gxYwbTp0/nH//4B8OH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",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Continent\n",
      "North America    6837887\n",
      "South America    2050948\n",
      "Unknown           761835\n",
      "Asia              740167\n",
      "Europe            434550\n",
      "Name: Encounter Count, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# 3. Sum of Encounters by Continent with a bar chart. Add title and labels. Use seaborn for styling. Print the results. Not horizontal. Display the results on top of the bars.\n",
    "encounters_by_continent = encounters_aor_df.groupby('Continent')['Encounter Count'].sum().sort_values(ascending=False)\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.barplot(x=encounters_by_continent.index, y=encounters_by_continent.values, palette='viridis')\n",
    "plt.title('Total Encounters by Continent')\n",
    "plt.xlabel('Continent')\n",
    "plt.ylabel('Total Encounters')\n",
    "plt.xticks(rotation=45)\n",
    "for index, value in enumerate(encounters_by_continent.values):\n",
    "    plt.text(index, value + 50, f'{value:,}', ha='center', va='bottom')\n",
    "plt.tight_layout()\n",
    "plt.show()\n",
    "print(encounters_by_continent)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "aab14e24",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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6tKly1FtO3fuVPXq1fXrr79mtMXHx/v+f3coe/BUkrQgMA9PhKSXnXNvmtkISXLOzZO0VN4S6ZvkLZM+OIR5AAAA8p3vv/9eTzzxhCTpiiuuUNu2bfXuu++qffv2mjBhgs/pAADI38444wx9+eWXR7V9+OGHIT1mxYoVdccdd+i2227Ts88+q88//1wffPCB1q494WwzJ3Xo0KHTHp4dsh48zrmvnXONnHP1nXN1nXNTA+3zAsUdOc/Nzrmazrl6zjkm1wEAAIVKvXr1NHLkSD322GPq06eP2rRpI8l7owcAAHKuVKlSkqTt27erVatWatiwoerWratVq1ZJkt566y01btxYDRo0UNu2bSVJn376qS699FI1atRIl156qf7v//4v22MMGzZM33//vVasWKFbbrlFc+bM0U8//aROnTqpSZMmatmypZKSvEFMb7zxhi6++GI1atRI7dq1044dOyRJU6ZM0bBhw9ShQwfdcMMNp33ezN4HAADgo0ceeUQffPCBVqxYoTvvvFP169eXJN17770+JwMAIP/7888/1bBhQ0lS9erVtWjRooz7nn/+eXXs2FF33nmnDh8+rH379um3337TTTfdpPfff1/Vq1dXcnKyJKl27dp6//33FRUVpf/+97+aNGmSXn311RMeNyIiQo899piuuOIKXXPNNWrVqpXatm2refPmqVatWvrkk08UHx+vxMREXXbZZfr4449lZnriiSd0//3368EHH5QkrV27Vh988IHOOOOM034sKPAAAAD4aNy4cdq5c6ciIyN15513av78+apQoYImT56sxMREv+MBAJCvZTVE64hmzZrpxhtv1MGDB9WtWzc1bNhQK1euVKtWrVS9enVJUrly5SRJu3bt0sCBA/Xdd9/JzHTw4MGTHvtIz6D4+Hjt2bNHH374oXr37p1x/19//SVJ2rp1q/r06aPt27frwIEDGceWpGuuuSZXijsSBR4AAABfrVmzRu+9954k6euvv1bv3r31wAMP+JwKAIDw16pVK73//vv6z3/+o+uvv17jx49XdHR0lqtT3XXXXWrTpo0WLVqkzZs3q3Xr1kEdIyIiQhEREUpPT1d0dHSWxaZRo0Zp7Nixuuaaa7Ry5UpNmTIl476SJUue4tllkSXX9gQAAIAcO3TokA4cOCBJql+/vhYtWqQpU6Zow4YNPicDACC8bdmy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DwAgT/Tu3VsdO3Y8arJlSdq2bZtPiQqv+Ph4Pfnkk4qKitLEiRO1YsUK3XnnnUpKSvI7GgAAQNhYv369pkyZoqioKI0ePVrNmzeX5H1p9thjj+V5Hgo8AIA8MXfu3CzbJ02alMdJkJ6erpo1a0qSnn/+ec2ePVt9+vTRvn37fE4GAAAQPo790iwxMdHXL80YogUAyBPLli2T5E1AN3r0aHXo0EEjRozQli1bfE5W+NStW/eox3306NEaMmSIdu3a5WMqAACA8HLkS7Nq1arp+eefV6lSpXz90owCDwAgT/z973+XJA0fPlxXXnml3nzzTQ0ePFiDBg3yN1ghNG/ePFWrVu2otg4dOjBECwAAIAfy25dmFHgAAHkiMjJS+/fv119//aXWrVuraNGiatasmQ4fPux3tEJn5cqVkqTU1FSNGzdOHTt21M0336zt27f7GwwAACCM5LcvzSjwAADyxP33368BAwbIzFS/fn31799fHTt21C233OJ3tEJn6tSpkrxx482aNdOSJUvUvXt3elMBAADkwA8//HDU5fvvv1eHDh30448/+pKHSZYBAHmiYcOGeuWVV/Tjjz9qx44dKlu2rGrVqqWoKP4rymvOOaWnp2v79u3q27evJKldu3aaNm2az8kAAADCR506ddS8eXOde+65krz3WN98842mTZum+fPn53keevAAAPJU9erVdckllyguLi6jJwnyXtu2bRUREaHU1FRJUlpaGqtoAQAA5MD333+vZs2aqXjx4ho/fryefPJJ1atXz5fijhTCHjxmNl9SF0k7nXN1s7jfJM2WdJWkfZIGOec+D1UeAIC/zjnnHJ1zzjmKiPC+W3DOacOGDVq5cqXef/99n9MVLitWrDiurXTp0vrss898SAMAABCeKleurJkzZ+r333/XrFmz9PPPP2v37t2+5QllD56nJHXK5v4rJdUKXIZJeiyEWQAAPnv44Yd1zjnnaPDgwUpMTNSqVat08cUXU9zxwbFL1nfs2JEl6wEAAE5R+fLlNX36dD3yyCOaNWuWbzlCVuBxzr0vKTmbTbpKetp5PpYUbWaVQpUHAOCvnj176vnnn1dsbKwGDBigRx55RAcPHvQ7VqF07JL1b7zxBkvWAwAA5ND333+vsWPH6r777tOOHTs0duxY3X///VqzZo0vefyc2fJsST9nur010HbcGq1mNkxeLx/FxsZmLO8KAAgvP/zwg9avX6+yZctq27ZtqlatGn/TfbB792698847+uWXXxQREaEPP/xQ6enpSk5O5vkIhQvuCf0xeN4AAMhzo0eP1k033aS0tDQ1atRIU6ZMUZkyZTRo0CDNmTMnz/OYcy50Ozc7V9KbJ5iD5z+SZjjnPgjcflfS7c65tdnts2nTps6vahgA4NRNmDBB+/btU8OGDbVixQoVL15cERERatGihW644Qa/4xUqX375paZPn679+/fr22+/VbNmzbRz507ddNNNuvbaa/2OV/BMKZsHx9gV+mMgbMyaNUtjxozRV199pVGjRsnMdOjQISUkJKhly5Z+xwOAAuOyyy7TBx98oPT0dF1wwQX67rvvJEmtWrUK6TQEZrbWOdf02HY/e/BslVQ10+0qkn7xKQsAIMQ+++wzvfvuu5KkG2+8Ue3bt9fy5cvVrl07Cjx5jCXrgYLt9ddf15gxYzR+/HjNnz9f5513nn7//Xd17dpVq1ev9jseABQYLVq0ULt27RQTE6PevXura9euio6OVr169XzJ4+c7udcl3WJmL0q6WNIu59xxw7MAAAVDxYoVNXPmTNWvX1/vvfeeLrzwQknS4cOHfU5W+Djn9Oabb+qjjz5SSkqKYmNj1blzZzVr1szvaAByQXJyshITE5WcnKzzzjtPkjcBqLeILQAgt8ycOVMpKSkqVaqUihQpoqSkJDnnFBcX50uekE2ybGYvSPpI0gVmttXMhpjZCDMbEdhkqaQfJG2S9C9J8aHKAgDw37PPPquaNWtq3bp1at68uR5++GFJ0nPPPedzssLnpptu0qZNmzK+cUpJSdHSpUuVkJDgdzQAuaB79+5atWqVrr76aqWmpkqS0tLSVLfucbMmAABOQ3Jysp599lktXLhQ+/fv18KFCzV//nz9+OOPvuQJ6Rw8ocAcPAAAnJ42bdpoxYoVGbfbtm2rd999N2PYHHIZc/AAAFAgdejQQYMGDVJqaqrmzZunKVOmKCYmRn/7299CunBFfpyDBwAA+KBevXoaOXKk6tevr5UrV6pNmzaSpEOHDvmcDEBu+Oijj3TvvfeqYcOGateunSZOnKhSpUpp6tSpat68ud/xAKDAOHDggPr16ydJmjNnjnr06CFJvg2JpQcPAACFzIEDB5SQkCAzU5cuXbR+/Xrt3r1b/fv3V3R0tN/xCh568CCPNW/eXC+//LJ2796tTp066eOPP1bJkiXVtWtXvffee37HA4AC4/rrr1exYsVkZtq/f7+io6NVrlw5ffPNN1q4cGHIjksPHgBAyG2sHdoJ5eKSNoZ0/4VFnz591KxZM6Wmpuq2225T586dFRMToz59+ujtt9/2Ox6A01SsWDFVreotVtusWTOdffbZkqTIyEg/YwFAgfPvf/9bCQkJatOmjVq0aKFnn31Wu3bt0mOPPeZLnpBNsgwAAPKn1NRUTZo0Sffff7927NihsWPHauDAgTpw4IDf0QDkgoYNG2asUPjaa69J8nrulS2bB73JAKAQ6dOnj6KiovTGG2+offv2+v3331WmTBn179/flzz04AEAoJApWbKkpk+frr/++kuVKlXSgw8+qHLlyqlYsWJ+RwOQC2bNmnVcW9GiRbVo0aK8DwMABdiRL80kqW7duho7dqwk6amnnvIlDz14AAAoZBYuXKg6deqod+/eev3111WyZEnt379fL730kt/RAOSCTz75RD169NCwYcO0fv16de7cWW3atNGyZcv8jgYABcqRL83uuuuujC/NnnzySd++NGOSZQBZWrFihaZMmaKIiAgNHz5cffv2lSR1796dbwBxQszBA2SBSZaRx1q0aKGFCxcqJSVFnTp10ieffKLSpUurffv2+vjjj/2OBwAFxp9//qm33npLNWvWVK1atbRgwQI559SvX7+QDotlkmUAOTJ58mQtW7ZMRYsW1ZQpU5SYmKi5c+cqNTXV72gAACAbhw8fVuXKlVWuXDlFRkYqNjZWkZGRioig8z4A5KYzzjhD3bt3z7g9YsQIH9NQ4AFwAs45lSlTRpKUkJCgxYsX66qrrlJycrLPyQAEI9S9qSR6VAH5Vb9+/dS4cWPVqlVLEydO1KWXXqqSJUvq6quv9jsaACCEKPAAyFKnTp20ZcsWVatWTZLUrVs31ahRQ7fffrvPyQAAQHZuvfVW3XrrrRm3+/Xrp4iICJUsWdLHVAAQfsLtCzP6aQLI0t13351R3Dmifv36euutt3xKBAAATkXp0qVVsmRJPfHEE35HAQCEED14AOTIqFGj9I9//MPvGAAA4AQSExOPa3POad68eRo6dKgPiQAAeYECD4As3X333ce1Oee0dOlSCjwAAORjvXr10pgxY3TsarkslAAABRsFHgBZ+ve//63nn3/+uPZly5b5kAYAAASrVatWGj58uGJjY49qZ6EEACjYKPAAyNLNN9+sCy+8UBUqVDiqPT4+3qdEAAAgGIsXL86yffbs2XkbBACQpyjwAMjSpEmTsmy/8cYb8zgJAADIiS+++EKNGjXSn3/+qXnz5ikpKUnVq1fXiBEjFB0d7Xc8AECIsIoWgCx98skn6tGjh4YNG6b169erc+fOatOmDUO0AADI58aNGydJGjFihM444wyNGzdONWrUUL9+/XxOBgAIJXrwAMjS2LFjtXDhQqWkpKhTp0765JNPVLp0abVv315XXnml3/EAAMAJmJmcc/r11181fPhwmZnOP/98zZ071+9oAIAQosADIEuHDx9W5cqVVa5cOUVGRio2NlaRkZGKiKDjHwAA+dnEiRN17bXXKjo6Wq1bt9Zll12mjRs3qnv37n5HAwCEEAUeAFnq16+fGjdurFq1amnixIm69NJLVbJkSV199dV+RwMAANnYt2+fnnrqKX366afasWOHypYtq//3//6fypcv73c0AEAIUeABkKVbb71Vt956a8btfv36KSIiQiVLlvQxFQAAOJkRI0aoWrVqio2NVffu3XXJJZfozDPP9DsWACDEGGsBICilS5dWyZIl9cQTT/gdBQAAZOOCCy7QRx99pIcffli///67unfvro4dO+rRRx/1OxoAIITowQMgS4mJice1Oec0b948DR061IdEAAAgJ6pXr65x48Zp3Lhx2rFjh5YsWeJ3JABACFHgAZClXr16acyYMXLOHdWemprqTyAAABCUCRMmHNcWGxurYcOG+ZAGAJBXKPAAyFKrVq00fPhwxcbGHtWenJzsUyIAABCMjh07+h0BAOADCjwAsrR48eIs22fPnp23QQAAAAAAJ0WBB0CWkpOT9dxzzykmJkY9evTQAw88oN27dys+Pl7Vq1f3Ox4AAAAAIBMKPACy1LdvXw0aNEipqam66KKLNGXKFMXExGjw4MFauXKl3/EAACi0NtaOC/kx4pI2hvwYAIDcRYEHQJYOHDigfv36SZLmzJmjHj16SJLMzM9YAIJ07cTQ/xe/LuRHAAAAQLAo8ADIUtWqVTV06FCZmZo0aaJRo0apXLlyKl++vN/RAAAAAADHoMADIEszZ87Ujh07dPbZZ+uDDz5QUlKSatSoobvuusvvaMjHQt1rhB4jAAAAQNYi/A4AIH8aMGCAGjVqpHvvvVefffaZmjZtqp9++ilj2BYAAAAAIP+gwAMgSxER3p+HDRs2aMaMGerQoYNuv/12/fbbbz4nA/y1YsUKXX755WrTpo1efPHFjPbu3bv7mAoAAACFHUO0AGRp4MCBGjp0qKpWraoBAwbo8ssv19dff62mTZv6HQ3w1eTJk7Vs2TIVLVpUU6ZMUWJioubOnavU1FS/owEAAKAQo8ADIEvXX3+92rZtq7fffls7duzQoUOHNHToUDVo0MDvaICvnHMqU6aMJCkhIUGLFy/WVVddpeTkZJ+TAQAAoDCjwAPghCpXrqzBgwf7HQPIVzp16qQtW7aoWrVqkqRu3bqpRo0auv32231OBgAAgMKMAg8AADlw9913H9dWv359vfXWWz6kAQAAADwUeAAAyIH169dr8uTJ2r17t9LT02Vmio6O1tSpU1WvXj2/4wHIBXv37lVKSoqio6NVqlQpv+MAABAUCjxAiOT3N4cba8eF/BhxSRtDfgwgr40cOVIvv/yyKlWqlNH2yy+/qE+fPlq1apWPyQCcrsTERE2bNk1lypRRmTJltHv3bqWlpWnSpElq166d3/EAAMgWBR4gl/HmECj4nHPZ3gYyO3f/8yE/xuaQH6FwuPvuu/XOO++oRIkSGW179+5Vhw4d+D8cAJDvUeABchlvDoGCbd68ebrllluUnJys9PR0RUREKCYmRo8++qjf0QCcpmLFimndunW6+OKLM9rWrVun4sWL+5gKAIDgUOABchlvDoGCrU6dOnrttdf8jgEgBJ599lklJCRowoQJOnz4sCIjI9WgQQM9/fTTfkcDAOCkKPAAuYw3h0DBtnPnTiUkJOiTTz5RcnKyzj//fLVs2VKjRo1SsWLF/I4H4DRUqlRJs2fP9jsGAACnhAIPkMt4cwgUbIMGDdK9996rBx54QImJiVq2bJmaNWum+Ph4/fvf//Y7HoDTcOwqeRERESpbtqzuuece1a9f3+94AABkK8LvAEBB89FHH+nqq6/W5MmTtXLlSjVv3lzt27fXhx9+6Hc0ALkgNTVVjRo1UmRkpFq0aKEvvvhCl19+uTZv3ux3NACnaeTIkXr00UeVmJiolStXKjExUXPnztXNN9/sdzQAAE6KHjxALhs7dqxefvll7d69W506ddLHH3+skiVLqmvXrnrvvff8jgfgNMXHx+vSSy9VlSpVtHnzZt19992SvLl5ABQ8rJIHAAgXFHiAXFasWDFVrVpVktSsWTOdffbZkqTIyEg/YwHIJQMGDNB1112nP/74Q+XLl1dEhNcZ9pFHHvE5GYDTdWSVvJSUFKWnp8vMWCUPABA2KPAAuaxhw4YZkysfWWnnwIEDKlu2rM/JAOSGP//8U0888YQ++ugjpaSkKDY2Vp07d1bv3r39jgbgNLFKHgAgnDEHD5DLZs2adVxvnaJFi2rRokU+JQKQm2644QZVqVJF06dPV8+ePXXWWWdp3759GjdunN/RAITI9OnT/Y4AAMBJ0YMHyGUrV65U69atlZqaqmnTpmnDhg2qWbOmJk+erEqVKvkdr9Dau3evUlJSFB0drVKlSvkdB2Hs119/Vffu3SVJ1apVU/v27ZWQkKB27dr5nAzA6Zo/f/5xbc45vfjii5o8ebIPiQAACB49eIBcNnXqVEneRKzNmjXT4sWL1b17dw0aNMjfYIVUYmKi2rRpo379+mnixInq37+/rrjiCv33v//1OxrCVJcuXXT11VfrjjvuULt27dS/f39JUrly5XxOBuB0TZgwQVFRUYqMjMy4REVFycz8jgYAwEnRgwfIZc45paena/v27erbt68kqV27dpo2bZrPyQqnu+++W++8845KlCiR0bZ371516NCBHhc4JXfccYcGDhyon376SePHj1f58uUlSS+//LLPyQCcrt69e6tjx46KjY09qn3btm0+JQIAIHgUeIAQaNu2rSIiIpSamqro6GilpaVp3759fscqlIoVK6Z169bp4osvzmhbt26dihcv7mMqhLPk5GQtXLhQMTExql+/vqZNm6bdu3crPj5e1atX9zsegNMwd+7cLNsnTZqUx0kAAPnBtRNDXzJZl4v7osAD5LIVK1Yc11a6dGl99tlnPqTBs88+q4SEBE2YMEGHDx9WVFSU6tevr6efftrvaAhTffv21aBBg5SamqqLLrpIU6ZMUUxMjAYPHqyVK1f6HQ/AaUhKSlLt2rV14MAB/fOf/8yYRy8+Pl4lS5b0Ox4AANmiwAPkst9//10LFixQnTp1VK9ePT3wwAMqUaKExowZo4oVK/odr9CpVKmSZs+e7XcMFCAHDhxQv379JElz5sxRjx49JIk5OoACID4+XomJiRo9erSqVaumMWPGaPXq1RowYACrYQIA8j0mWQZy2XXXXacKFSpo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fbfeeecdlShRIqNt79696tChAxPKolDr3bu3OnbseNRky5K0bds2nxIVDBR4kK88/vjjmj9/vkqVKqX+/ftrwYIFioyMVJs2beiqh1PSrl07FS9eXD///LMOHz6siIgIXXjhherfv7/f0YKWebWsJk2aqEmTJpo+fbq+/fZbH1MB/ouPj9ell16qqlWr6scff9Tdd98tSapTp47PyQDAU6xYMa1bt04XX3xxRtu6detUvHhxH1MB/ps7d26W7ZMmTcrjJAVLoS/wrFixQlOmTFFERISGDx+uvn37SpK6d++uRYsW+Zyu8Hnqqaf08ccf688//9SFF16o7777TlFRUWrRogUFHpySIUOGSJKKFi2q3377TZUrV1aZMmU0bNgwPf744z6nC86LL76YZfv555+fx0mA/GXAgAG67rrr9Mcff6h8+fIZc1Q98sgjPicDkBtiYmLUuXNn9ejRQ506dQrLosizzz6rhIQETZgwQYcPH1ZkZKQaNGigp59+2u9ogK9ONMckTk+hL/BMnjxZy5YtU9GiRTVlyhQlJiZq7ty5Sk1N9TtaoZSenq5t27YpJSVFzjnt3LlTZcuWzVgiGsipTZs26b333pMk1atXT6+88ookqU2bNn7GypFju64e8cYbb+jqq6/O4zRA/hIZGamKFSse1fbEE09o6NChPiUCkFvq16+vsWPHatGiRZoxY4aqVKmi7t276+qrr1bZsmX9jheUSpUqafbs2X7HAPKdt956S+np6brtttvUoEED9ejRQx06dGCRhNNU6As8zjmVKVNGkpSQkKDFixfrqquuUnJyss/Jcqag9ES6//77FR8fr7p16+rll1/Wddddp6ioKN1zzz1+R0OYOnToUMb1++67L+N65mFP+d0PP/xwXJtzTvfffz8FHhRqiYmJx7U55zRv3jwKPEABYGZq2LChGjZsqHvuuUebNm3SokWL1LVrV61cudLveEH59ttvdffdd+uHH37Qxo0b1aJFC8XFxenuu+/WmWee6Xc8wDfMMRkahb7A06lTJ23ZskXVqlWTJHXr1k01atTQ7bff7nOynCkoPZFatWqlVq1aZdw+0vMCOFWPP/54RpfoI8WQAwcOaOzYsT4nC17Dhg3Vq1ev44pSP/74o0+JgPyhV69eGjNmzHGvjXD7vw9A1ho0aHDU7fPOO0/jx4/X+PHjfUqUcyNH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gKMdeZ9eo0aNjLYiRYpkrJwXDq655hp16dJFrVu3VpkyZbR792699957uuaaa/yOVmi1bdtWERERSk1NVXR0tNLS0rRv3z6/YwG5otAXeGbNmqUVK1bo119/VadOndSjRw/Vq1fP71g5VlB6Ih04cED9+vWTJM2ZM0c9evSQ5H1bAwAAgMKjILxPHz9+vJo3b65169apdOnSqlKligYOHKgffvjB72iF0ooVK45rK126tD777DMf0pyaGTNmaOLEifr44481fvx4RUZG6tChQ5o8ebI6derkdzz4rNAXeKpVq6ZFixZp3759WrZsmWbOnKmkpCRdccUVuv/++/2OF7TU1FSdddZZOuuss/Tmm29mTBjWq1evsCqOVK1aVUOHDpWZqUmTJho1apTKlSuXUbACAABA4VAQ3qePGzdOO3fuVGRkpP744w/Nnz9fFSpUUJ8+fZSYmOh3vELn+++/16OPPqqYmBgNGTJEkyZN0u7duzVhwgQ1adLE73hBeffddzVx4kTdeeedevXVV1WxYkXt3btX7dq1o8ADCjxHlChRQj179lTPnj116NChsPuD26NHDyUmJmrixIlKTU1V165dtXr1ai1dulRPPvmk3/GC9vTTT+vLL7/U2WefrfLly+udd96Rc05dunTxOxryKYY2AQBQsIXz+/Q1a9bovffekyR9/fXX6t27tx544AGfUxVeN954o2bMmKGUlBQ1b95cr7zyisqVK6f+/ftr9erVfscLSkxMjL799ltVqVJFqampqlixotLS0lS8eHG/oxVI4TatRaEv8MyaNeu4tqioqONWcgoXH374YcZ/Ip06ddLll1/uc6Kccc6pQYMGGbc7dOgg55w6deqk5cuX+5gMAAAAeakgvE8/dOiQDhw4oKJFi6p+/fpatGiRBgwYoA0bNvgdrVA6fPiwLr30UqWnpysyMlKNGzeWJEVGRvqcLHjz5s3TPffco23btqlhw4a64IILdP755+vRRx/1OxrygUJf4KlXr57S09OPanPOadKkSWFVUPj888/VsmVLbdy4MWPCsPT0dO3Zs8fvaDlSqlQpXXLJJXLOSfLm3nHO6euvv/Y5GQAAAPJSQXif/vDDD2f0spCkM888U6+//roWLlzoc7LCqUWLFmrXrp1iYmLUu3dvde3aVdHR0WE1t9OZZ56ZZfETkCjwHFVQODJXTTgW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2g4gIiImtUvX4/16zm07yEAiIiZxFnA18BFgPdsr2l6p878txxYRETEWkuCJiBhumuBxv+cREa2w/QrgRcDtwOck/UDSW5uR4xERETEASfBERAw3T/C43/OIiNbYvsP2F4DtgKOBg4A3tBpURETEGEkPnoiIIdY1XrV7tCrN82VtL9VWbBER3SRtThmR/hzgx8BXbP+o3agiIiLGRxI8ERERETErkm4G/gScCJwN3Nt93vYlg48qIiJivCTBExERERGzIulcJi4bte2tBxhORETEWEqCJyIiIiIiIiKicg9pO4CIiIiIqJuk505y2unFExER8eDLDp6IiIiImBVJ3+xz2MCGwKq2lxxwSBEREWMnO3giIiIiYlZsv7T7uaRnAwcAvwH2aiWoiIiIMZMET0RERETMCUnPBw6k7N452Pb3Wg4pIiJibCTBExERERGzIml7yo6dO4ADbJ/XckgRERFjJz14IiIiImJWJN0P3ApcRp9x6bZfNvCgIiIixkx28ERERETEbG3VdgARERHjLjt4IiIiIuJBIWk1YBfbh7UdS0RExKhbou0AIiIiImJ0SHqkpLdI+iFwLvCYlkOKiIgYCynRioiIiIhZkbQisAOwG7AucCqwlu1VWw0sIiJijKREKyIiIiJmRdKdwAXA+4Af27akG22v1XJoERERYyMlWhERERExW/sDywJHAftJWrvleCIiIsZOdvBERERExJyQtBawK7AL8ETgA8Cptn/WamARERFjIDt4IiIiImJWJO0EYPtG2x+1vT6wGfAw4MxWg4uIiBgT2cETEREREbMi6XTK8I632r6x7XgiIiLGURI8ERERETFrkl4BfAz4MqUXz/2dc7b/0FJYERERYyMJnoiIiIiYE5I2BH4I/BHoXGQ607QiIiIefA9pO4CIiIiIqJukZSgj0l8N7G779JZDioiIGDtpshwRERERs3U5sCTwtCR3IiIi2pESrYiIiIiYFUlPsX1123FERESMsyR4IiIiImJWJJ022XnbLxtULBEREeMqPXgiIiIiYraeBfwSOAH4KaB2w4mIiBg/2cETEREREbMiaUlgG2BXYAPgDOAE21e1GlhERMQYSZPliIiIiJgV2/fZ/rbt1wPPBG4AzpX0/1oOLSIiYmykRCsiIiIiZq0Zlb49ZRfPmsARwCltxhQRETFOUqIVEREREbMi6XhgPeBM4ETbV7YcUkRExNhJgiciIiIiZkXS/cDfmqfdF5cCbHulwUcVERExXpLgiYiIiIiIiIioXJosR0RERERERERULgmeiIiIiIiIiIjKJcETEREREREREVG5JHgiIiJiJEhaRdKJkn4u6WpJ35L0XElfbc5vJOnFXX//ZZLeO4C4zpW0aZ/jm0o64sH+9yMiImI8PKTtACIiIiJmS5KAU4Hjbe/SHNsIWNH2q5u/thGwKfAtANunAacNPNiG7YuAi9r69yMiImK0ZAdPREREjIKtgH/YPrpzwPZ84JeSrpS0NHAQsLOk+ZJ2lvQGSZ8BaI51/twp6XmSVpB0rKQLJV0q6eXN332DpFMkfVvS9ZIObY4vKem45t+7QtI7uuLbUdIFkn4m6TnN399S0unN4w9K+qKks5v/zz0H8R8tIiIiRkd28ERERMQoWA+4eKKTtu+R9H5gU9t7QUnUdJ3fqDn2UuA9wP8CHwLOtv1GSQ8HLpD0/eZLNgI2Bu4GrpN0JPBo4PG212v+vx7eFcJDbD+9KRH7APCCPmFuADwTWAG4VNIZtn89jf8GERERMcaygyciIiICkPRE4DBgZ9v/AF4IvFfSfOBcYFlg9eavn2X7Dtt3AVcDawA3AmtJOlLStsCfu/7vT2n+92JgzQlC+IbtO23/DjgHePpcfW8REREx+pLgiYiIiFFwFbDJTL9Y0grAScCeXbtmBLzK9kbNn9VtX9Ocu7vry++j7ND5I7AhJRn0NuC/uv7O3d1/d4IwvJjnERERERNKgiciIiJGwdnAMt29ayRtRtlZ0/EXYMUJvv4LwBds/6jr2HeA/9c0cEbSxpMFIOmRwBK2vwYcCDxtmt/DyyUtK+kRwJbAhdP8+oiIiBhjSfBERERE9Wwb2AHYphmTfhXwQaC7h805wFM6TZY7ByWtAbwaeGNXo+VNgQ8DSwGXS7qyeT6ZxwPnNiVdxwH7TfPbuAA4Azgf+HD670RERMR0qFwPRURERERbJH0Q+Kvtw9uOJSIiIuqUHTwREREREREREZXLDp6IiIiIiIiIiMplB09EREREREREROWS4ImIiIiIiIiIqFwSPBERERERERERlUuCJyIiIiIiIiKicknwRERERERERERULgmeiIiIiIiIiIjK/X9dZM+EeaoJqgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1152x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 4. Group by Fiscal Year and Citizenship, then sum Encounter Count\n",
    "grouped_data = encounters_aor_df.groupby(['Fiscal Year', 'Citizenship'])['Encounter Count'].sum().reset_index()\n",
    "\n",
    "# Create a pivot table\n",
    "pivot_table = grouped_data.pivot(index='Citizenship', columns='Fiscal Year', values='Encounter Count').fillna(0)\n",
    "\n",
    "# Sum across fiscal years for annotation\n",
    "total_by_citizenship = pivot_table.sum(axis=1)\n",
    "\n",
    "# Plot as stacked bar chart\n",
    "ax = pivot_table.plot(kind='bar', stacked=True, figsize=(16, 8))\n",
    "\n",
    "# Add total labels on top of each bar\n",
    "for idx, total in enumerate(total_by_citizenship):\n",
    "    ax.text(idx, total + total_by_citizenship.max() * 0.01, f'{int(total)}', ha='center', va='bottom', fontsize=8, rotation=90)\n",
    "\n",
    "plt.title('Sum of Encounter Count by Citizenship and Fiscal Year (with Totals)')\n",
    "plt.xlabel('Citizenship')\n",
    "plt.ylabel('Total Encounter Count')\n",
    "plt.xticks(rotation=90)\n",
    "plt.legend(title='Fiscal Year')\n",
    "plt.tight_layout()\n",
    "plt.grid(axis='y')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d7453a15",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "hovertemplate": "Fiscal Year=%{x}<br>Total Encounters=%{text}<extra></extra>",
         "legendgroup": "",
         "marker": {
          "color": "#636efa",
          "pattern": {
           "shape": ""
          }
         },
         "name": "",
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "text": [
          1956519,
          2766582,
          3201144,
          2901142
         ],
         "textposition": "auto",
         "type": "bar",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          1956519,
          2766582,
          3201144,
          2901142
         ],
         "yaxis": "y"
        },
        {
         "line": {
          "color": "red",
          "dash": "dash"
         },
         "mode": "lines+markers",
         "name": "Mean",
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "y": [
          2706346.75,
          2706346.75,
          2706346.75,
          2706346.75
         ]
        },
        {
         "line": {
          "color": "blue",
          "dash": "dash"
         },
         "mode": "lines+markers",
         "name": "Median",
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "y": [
          2833862,
          2833862,
          2833862,
          2833862
         ]
        }
       ],
       "layout": {
        "barmode": "relative",
        "legend": {
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Total Encounters by Fiscal Year with Mean and Median"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Fiscal Year"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Total Encounters"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Fiscal Year  Encounter Count        Mean     Median\n",
      "0         2021          1956519  2706346.75  2833862.0\n",
      "1         2022          2766582  2706346.75  2833862.0\n",
      "2         2023          3201144  2706346.75  2833862.0\n",
      "3         2024          2901142  2706346.75  2833862.0\n"
     ]
    }
   ],
   "source": [
    "# 5. Calculate the mean and median of the Sum of Encounter Count by Fiscal Year. Add interactive table with plotly. Add meand and median results to the table.\n",
    "encounters_by_fiscal_year_stats = encounters_by_fiscal_year.copy()\n",
    "encounters_by_fiscal_year_stats['Mean'] = encounters_by_fiscal_year_stats['Encounter Count'].mean()\n",
    "encounters_by_fiscal_year_stats['Median'] = encounters_by_fiscal_year_stats['Encounter Count'].median()\n",
    "import plotly.express as px\n",
    "fig = px.bar(encounters_by_fiscal_year_stats, x='Fiscal Year', y='Encounter Count',\n",
    "             title='Total Encounters by Fiscal Year with Mean and Median',\n",
    "             labels={'Encounter Count': 'Total Encounters'},\n",
    "             text='Encounter Count')\n",
    "fig.add_scatter(x=encounters_by_fiscal_year_stats['Fiscal Year'], y=encounters_by_fiscal_year_stats['Mean'],\n",
    "                mode='lines+markers', name='Mean', line=dict(color='red', dash='dash'))\n",
    "fig.add_scatter(x=encounters_by_fiscal_year_stats['Fiscal Year'], y=encounters_by_fiscal_year_stats['Median'],\n",
    "                mode='lines+markers', name='Median', line=dict(color='blue', dash='dash'))\n",
    "fig.update_layout(yaxis_title='Total Encounters', xaxis_title='Fiscal Year')\n",
    "fig.show()\n",
    "\n",
    "print(encounters_by_fiscal_year_stats)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "aa5ca677",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Fiscal Year  Encounter Count        Mean     Median  Standard Deviation  \\\n",
      "0         2021          1956519  2706346.75  2833862.0       531864.471472   \n",
      "1         2022          2766582  2706346.75  2833862.0       531864.471472   \n",
      "2         2023          3201144  2706346.75  2833862.0       531864.471472   \n",
      "3         2024          2901142  2706346.75  2833862.0       531864.471472   \n",
      "\n",
      "       Variance  \n",
      "0  2.828798e+11  \n",
      "1  2.828798e+11  \n",
      "2  2.828798e+11  \n",
      "3  2.828798e+11  \n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAsgAAAGoCAYAAABbtxOxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAABnZUlEQVR4nO3deXzddZX/8de52dPs3dt0pWsKbcGyFRUEdRRXFBwVRNABEdRxZvg5jjPjNq78ZvyhsgkquDAuw+A6bgOiiCDK0gJtui+0dKPNvif3nt8f3+9NbtKbNG1zc5e8n4/HfTS593vv/TTf3OSdzz2f8zF3R0REREREApF0D0BEREREJJMoIIuIiIiIJFBAFhERERFJoIAsIiIiIpJAAVlEREREJIECsoiIiIhIAgVkkQnGzNzMFqV7HNnGzC4ws70pfo5fmtm7U/j4WXnuzexyM/vNCLen/NycLDObH37984/zfi8zs82pGpeIJKeALJIhzKwt4RIzs86Ezy8f5j5jGgzM7Hdm1jVkLD8bq8cfa2Z2j5l9Jt3jOF7huHuGfJ3/2t1f6+7fSsN4PmtmDw65bomZtZjZaeM9nqHc/V53f3X885MJ+ma2IeFrHh3y/f6xsRv1cY9rl5m9cuj17v4Hd1+ajjGJTGTH9ZesiKSOu5fFPzazXcDfuPsDaRjKB9z962l43nFnZvnu3pemp7/J3f8lTc891KeBp8zsGne/y8wMuAv4krs/OxZPkOavdT93XxH/2Mx+B3w32fd7poxXRNJDM8giGc7MiszsZjPbF15uDq+bBPwSmJUwAzbLzM4ys8fMrMnM9pvZLWZWOAbjuMDM9prZP5jZofCxr064vcTM/sPMdptZs5k9YmYl4W1vDGfumsJZ6uUJ9xs0G5g4KzzSc5rZtcDlwEcSZ7rDr8F/m9mLZrbTzD6U8NifNLP7zOy7ZtYCXBV+vZ4IZ0sPmtmXjvF1+JiZHQ5n/C4PrzszvG9+wnFvNbN1x/k1/p2Z/U348SIz+334tTxsZj9IOG6Fmf2vmTWEz/ux8PoTOvfu3g28B/iCmc0GrgWqgc+a2bKE59psZm9LGMfrzOzp8Gu3x8w+mXBbvKTgvWb2PPDbJP/f35vZW8OPXxoef3H4+SvjXz8zu8rMHgk/fji8+/rwvP91wuMl/d4cjeHGa2bvMbN6M2s0s1+b2byE+7iZXWdmW8PbbzUzC2/LM7N/D8/dDuB1xzOehOcY9C5R+H13o5k9E35v/MDMihNuf72ZrQu/Bx41s5Un8rwiE50Cskjm+2fgHGA1sAo4C/gXd28HXgvsc/ey8LIPiAJ/B0wBzgUuAq4fo7HMACqB2cB7gVvNrDq87d+BlwBrgRrgI0DMzJYA3wM+DEwFfgH8bDTBbaTndPc7gXsJZmLL3P0NZhYBfgasD4+/CPiwmf1VwuO9CbgPqArv/2Xgy+5eAZwC/PAYY5kSPva7gTvNbKm7/wU4Arwq4dgrgO+M8v+YzL8BvyEIqrXAVwHMrBx4APgVMAtYBMTLI0743Lv748A9wLeBzxIE5kLgf4H/BKYB7wBuM7P4LGw7cCXB1/J1wPvN7M1DHvp8YDnwVxzt98AF4ccvB3aEx8c//32Scb48/HBVeN7jfziM9L15PPrHG/5fPga8heB79w8E38uJXg+cSfDafBsD/89rwttOB9YAl57AWIbzNuA1wAJgJXAVgJmdAXwTeB8wGfga8FMzKxrD5xaZELIyIJvZN8NZgudGefzbzGyjBTNY/5nq8YmMscuBT7v7IXd/EfgU8K7hDnb3J939T+7e5+67CH5Jnj/c8Ul8JZx9il/+LeG23nAsve7+C6ANWBoG0/cAf+vuL7h71N0fDWcm/xr4H3f/X3fvJQjSJQRBejSSPucwx54JTHX3T7t7j7vvICgVeHvCMY+5+4/dPebuneHjLzKzKe7e5u5/OsZ4/tXdu93998D/EIQVgG8RhGLMrIYgKI308+bGhK/x4WH+3/OAWe7e5e6PhNe/Hjjg7v8RXt8ahtuxOPf/QhC4v+PuT4TPtcvd7w4f8yngvwnDnrv/zt2fDb+WzxCEx6HP90l3bw+/1kP9nsGB+PMJn59PkoA8guP5PhlJ4njfB3ze3evDcovPAasTZ5GBL7h7k7s/DzxE8IcsBN8XN7v7HndvCP9vY+Ur7r4vfNyfJTznNcDX3P3x8DX4LaCb4A9sETkOWRmQCWY5XjOaA81sMfBPwHlh7dmHUzcskZSYBexO+Hx3eF1SFiyu+rmZHbCgjOBzBDOKo/Uhd69KuPxrwm1HhtRldgBl4eMXA9uPNX53jwF7CGb6RmO450xmHkHJSX/AJ5gBnJ5wzJ4h93kvsATYZGZ/MbPXjzCWxnDmPi7xXHwXeIOZlRGEoz+4+/4RHuvfE77Gyc7PRwAD/hz+cf+e8Po5JP86n/S5D0PhTmBDeNU84OwhX8/LCWZrMbOzzewhC8pZmoHrkjzf0K93oseAJWY2nSDkfRuYY2ZTCN4peXiE+w51PN8nI0kc7zzgywn/9waCc5L4vXtgmOecNeSxEl/DJ2u455wH/MOQ8zWHEX5eiEhyWRmQ3f1hgh9U/czsFDP7lZk9aWZ/MLNl4U3XALe6e2N430PjPFyRk7WP4Bdf3NzwOgBPcvztwCZgcVg28DGCX+qpdBjoIihRGGrQ+MMazTnAC+FVHUBpwvEzjuN5h/7/9wA7hwT8cne/eLj7uPtWd38HQQnBF4H7LKjvTqZ6yG3958LdXyAIfJcQzPCfTHkF7n7A3a9x91kEM5m3WVCrvYfkX2cY+3O/B/j9kK9nmbu/P7z9P4GfAnPcvRK4I8nzJfseDW5w7wCeBP4WeM7de4BHgb8Htrt7spn1VEsc7x7gfUP+/yXu/ugoHmc/wfd53NwxHWVye4DPDhlvqbsPLQsRkWPIyoA8jDuBD7r7S4AbgdvC65cQzFD80cz+ZGajmnkWySDfA/7FzKaGM2sfJ5itBDgITDazyoTjy4EWoC38Q/H9pFg4K/xN4EsWLJLLM7Nzw9rHHwKvM7OLzKwA+AeCt33jIWMd8M7wPq/h+EoCDgILEz7/M9BiZv9owaLBPDM71czOHO4BzOwKM5sa/h+awqujIzznp8ys0MxeRlCC8F8Jt32bYOb3NOBHx/H/SDauy8ysNvy0kSC4RYGfAzPM7MMWLNYsN7Ozw+PG+tz/nODn57vMrCC8nGkDiyzLgQZ37zKzs4B3nsBz/B74AAPlFL8b8nkyQ897qtwB/FO85trMKs3sslHe94fAh8ysNqyF/ugo7lNgZsUJl+PtNHUXcF04s29mNsmChZTlx/k4IhNeTgTk8C3NtcB/WbDq+WvAzPDmfGAxwUKQdwBfN7Oq8R+lyAn7DPAE8AzwLPBUeB3uvokgQO8I31KdRfAH4juBVoJfmD9I9qAjuMUG9+d9cpT3uzEc318I3uH5IhBx980EtblfJZhpfgPwhnC2EILZwzcQhNPLgR8fx1i/AdSF//cfu3s0fKzVBKUCh4GvEyzeGs5rgA1m1kawYO/t7t41zLEHCMLqPoIFfteF5yDuRwSz5T8aUopxIs4EHg/H9VOC+u6d7t5KsBjwDeF4tgKvCO9zsud+kPC5Xk1Qw70vfL4vAvFFX9cDnzazVoI/3EZa4Dic3xME7YeH+TyZTwLfCs/720Y47qS4+48I/r/fD0tWniNYGDsadwG/Jlgw+hRw/yju8wugM+HyyeMc7xME75reQvB9uo1wAZ+IHB9zH/bdr4xmZvOBn7v7qWZWAWx295lJjrsD+JO73xN+/iDwUQ9WnYuIjCkz207wtnw6eliLiMgYyIkZZHdvAXbG3/oK31paFd78Y8LZlfDt6SUErYRERMaUBT19nSQ9f0VEJHtkZUA2s+8RLIZZasEmAu8leGv2vWa2nmAF9pvCw38NHDGzjQQteP6Pux9Jx7hFJHdZsCvb7cANYT2ziIhkqZSXWJhZHkH95Avu/voht10A/ISgVhDgfnf/dEoHJCIiIiIyguNdIXsi/haoByqGuf0PQ4OziIiIiEi6pDQghy2KXkewbenfj8VjTpkyxefPnz8WDyUiIiIiWezJJ5887O5Tx/pxUz2DfDNBT9CRejCeG9YN7wNudPcNQw8ws2uBawHmzp3LE088kYKhioiIiEg2MbOx3KWyX8oW6VmwXeshdx+ph+pTwDx3X0XQI/XHyQ5y9zvdfY27r5k6dcz/SBARERER6ZfKLhbnAW80s13A94ELzey7iQe4e4u7t4Uf/4JgF6EpKRyTiIiIiMiIUhaQ3f2f3L3W3ecT7ML0W3e/IvEYM5thZhZ+fFY4HrVgExEREZG0GY8uFoOY2XUA7n4HcCnwfjPrI9hW8+2erVv7iYiISNr19vayd+9eurqG2zFeslFxcTG1tbUUFBSMy/Nl3VbTa9ascS3SExERkWR27txJeXk5kydPJnyTWrKcu3PkyBFaW1tZsGDBoNvM7El3XzPWz5mVO+mJiIiIJNPV1aVwnGPMjMmTJ4/ruwIKyCIiIpJTFI5zz3ifUwVkEREREZEECsgiIiIiY+TIkSOsXr2a1atXM2PGDGbPnt3/eU9Pz6Bjb775Zjo6Oo75mBdccEHSTdIuuOACli5d2v/4l1566Zj9P07U5z73uXQPYUyMexcLERERkUwRizlH2nvo6YtSmJ/H5EmFRCIn/nb+5MmTWbduHQCf/OQnKSsr48Ybb0x67M0338wVV1xBaWnpCT/fvffey5o1Y75G7YR97nOf42Mf+9hx3ScajZKXl5eiEZ0YzSCLiIjIhBSLOZsPtnLJbX/kvC8+xCW3/ZHNB1uJxca2w9eDDz7I6aefzmmnncZ73vMeuru7+cpXvsK+fft4xStewSte8QoA3v/+97NmzRpWrFjBJz7xiRN+vquuuooPfehDrF27loULF3Lffff133bTTTdx2mmnsWrVKj760Y8CsG7dOs455xxWrlzJJZdcQmNjIzB45vrw4cPMnz8fgHvuuYe3vOUtvOY1r2Hx4sV85CMfAeCjH/0onZ2drF69mssvvxyA7373u5x11lmsXr2a973vfUSjUQDKysr4+Mc/ztlnn81jjz3GRz/6Uerq6li5cuWwf1CMJ80gi4iISE761M82sHFfy7C3f+iixfzjfz/D3sZOAPY2dnLNt5/gi29dyVce3Jr0PnWzKvjEG1aMegxdXV1cddVVPPjggyxZsoQrr7yS22+/nQ9/+MN86Utf4qGHHmLKlGAT4c9+9rPU1NQQjUa56KKLeOaZZ1i5cuWIj3/55ZdTUlICwKte9Sr+7//9vwDs37+fRx55hE2bNvHGN76RSy+9lF/+8pf8+Mc/5vHHH6e0tJSGhgYArrzySr761a9y/vnn8/GPf5xPfepT3HzzzSM+77p163j66acpKipi6dKlfPCDH+QLX/gCt9xyS/8Men19PT/4wQ/44x//SEFBAddffz333nsvV155Je3t7Zx66ql8+tOfpqGhgfe+971s2rQJM6OpqWnUX99U0QyyiIiITEilhXn94Thub2MnpYVj93Z/NBplwYIFLFmyBIB3v/vdPPzww0mP/eEPf8gZZ5zB6aefzoYNG9i4ceMxH//ee+9l3bp1rFu3rj8cA7z5zW8mEolQV1fHwYMHAXjggQe4+uqr+0s6ampqaG5upqmpifPPP/+Y40t00UUXUVlZSXFxMXV1dezevfuoYx588EGefPJJzjzzTFavXs2DDz7Ijh07AMjLy+Otb30rABUVFRQXF/M3f/M33H///SdVcjJWNIMsIiIiOelYM70vtnZTW10yKCTXVpdQW13KD9537piMYdKkSaM6bufOnfz7v/87f/nLX6iuruaqq646qb6/RUVF/R/HN4Vz9+Nql5afn08sFgM4aiyJj5+Xl0dfX99R93d33v3ud/P5z3/+qNuKi4v7647z8/P585//zIMPPsj3v/99brnlFn7729+OepypoBlkERERmZAmTyrkrivXUFsdlCjUVpdw15VrmDypcMyeo6uri127drFt2zYAvvOd7/TP1paXl9Pa2gpAS0sLkyZNorKykoMHD/LLX/5yzMYQ9+pXv5pvfvOb/Z0zGhoaqKyspLq6mj/84Q9HjW/+/Pk8+eSTAIPqmEdSUFBAb28vEMwy33fffRw6dKj/+ZLNNLe1tdHc3MzFF1/MzTff3F+iMaxoFA4fhvBxU0EzyCIiIjIhRSLG0unl/Oj688asi8VQxcXF3H333Vx22WX09fVx5plnct111wFw7bXX8trXvpaZM2fy0EMPcfrpp7NixQoWLlzIeeedN6rHT6xBnjJlCg888MCwx77mNa9h3bp1rFmzhsLCQi6++GI+97nP8a1vfYvrrruOjo4OFi5cyN133w3AjTfeyNve9ja+853vcOGFF45qPNdeey0rV67kjDPO4N577+Uzn/kMr371q4nFYhQUFHDrrbcyb968QfdpbW3lTW96E11dXbg7/+///b/kD+4ehOLm5uDj8vJRjelEWHzaPVusWbPGk/UCFBEREamvr2f58uXpHoaMpVgMotHg3BYXD1xfXo7NmvWku495nzvNIIuIiIhI5gmDMWFruPGkgCwiIiIimSMWg76+4N80UUAWERERkfTLgGAcp4AsIiIiIukTL6PIgGAcp4AsIiIiIuMvGg1mjDOwYYQCsoiIiIiMnwwOxnHaKERERERkjBw5coTVq1ezevVqZsyYwezZs/s/7+npGZPnuOqqq5Ju3JHs+n379nHppZeOyfOeFPcgFHd3Q29vRodj0AyyiIiIyJiZPHly/05wn/zkJykrK+PGG2/sv72vr4/8/PGLX7NmzRr1Lngp4T5QY5zhoTiRArKIiIjknr4+2Ls3NY9dWwvHEXKvuuoqampqePrppznjjDO4/vrrueGGG3jxxRcpLS3lrrvuYtmyZVx11VVUVFTwxBNPcODAAW666SYuvfRS3J0PfvCD/Pa3v2XBggUczyZvu3bt4vWvfz3PPfcc99xzDz/96U/p6Ohg+/btXHLJJdx0000A/OY3v+ETn/gE3d3dnHLKKdx9992UlZUd95emXzwY9/Wd+GOkkQKyiIiI5J69e2HBgtQ89s6dMH/+cd1ly5YtPPDAA+Tl5XHRRRdxxx13sHjxYh5//HGuv/56fvvb3wKwf/9+HnnkETZt2sQb3/hGLr30Un70ox+xefNmnn32WQ4ePEhdXR3vec97Tmjo69at4+mnn6aoqIilS5fywQ9+kJKSEj7zmc/wwAMPMGnSJL74xS/ypS99iY9//OPH/wRZHozjFJBFREREUuyyyy4jLy+PtrY2Hn30US677LL+27q7u/s/fvOb30wkEqGuro6DBw8C8PDDD/OOd7yDvLw8Zs2axYUXXnjC47jooouorKwEoK6ujt27d9PU1MTGjRs577zzAOjp6eHcc889vgeO1xinYde7VFBAFhERkdxTWxvM9KbqsY/TpEmTAIjFYlRVVfXXKQ9VVFTU/3FiKYWZHfdzHuvx8/Ly6Ovrw9151atexfe+973jf8AcC8ZxCsgiIiKSe/Lzj7sMYjxUVFSwYMEC/uu//ovLLrsMd+eZZ55h1apVw97n5S9/OV/72te48sorOXToEA899BDvfOc7x2xM55xzDjfccAPbtm1j0aJFdHR0sHfvXpYsWTL8nWKxgcV3OUht3kRERETG0b333ss3vvENVq1axYoVK/jJT34y4vGXXHIJixcv5rTTTuP9738/559//rDHvu9976O2tpba2tpRl0lMnTqVe+65h3e84x2sXLmSc845h02bNiU/OBaDnp7gkqPhGMCOZyVkJlizZo0/8cQT6R6GiIiIZKD6+nqWL1+e7mHknlgsKKVI43bQ9Vu2sLy4eOCK8nJs1qwn3X3NWD+XSixEREREJLl4GUUag3E6KCCLiIiIyGATNBjHKSCLiIhITnH3Mev6MOHEexhnWAnueJcEa5GeiIiI5Izi4mKOHDky7oEqq8U39+juht7ejAzHRxobKR7HP3o0gywiIiI5o7a2lr179/Liiy+meyjZIRYLLhkWiocqNqO2oGDcnk8BWURERHJGQUEBC1K1xXSucIemJmhszPotoVNFAVlERERkIojFBoJxDvcwHgsKyCIiIiK5LBoNQnFT04TtSnG8FJBFREREclFfXxCMm5sVjI+TArKIiIhILunthYYGaGnJ+MV3mUoBWURERCQX9PQEwbi1VcH4JCkgi4iIiGSz7u6BYCxjQgFZREREJBt1dgbBuL093SPJOQrIIiIiItmkoyMIxh0d6R5JzlJAFhEREckG7e1w5Ah0daV7JDlPAVlEREQkk7W2BjPG3d3pHsmEoYAsIiIikmncB4JxT0+6RzPhKCCLiIiIZAr3YGOPxsagn7GkhQKy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yTPjsiUVXHdaNXPKM6xV2dASifissEokRERERE6KAnLoucNd3LK+gV/vbqc437i6roprTqtmemkGfIny8gYvmot3kRARERGRMZcB6S+9njjYyS3rG/jd3g7KCyN8YFUNV6+ooqY4TVseq0RCREREJK0mZPJydx7Z18Et6xt5/EAnNcV5/J+XTOZdyyupKBynYByJBGF46MxwLrSKExEREcliEyogx9x54Pl2bl3fwPrD3UwvzeNfz57CO5ZUUlqQwtrd/PzkG22IiIiISMZJWUA2sznAt4EZQAy4092/POQYA74MXAx0AFe5+1NjPZZozPmfXW3cur6BzY09zC0v4HNrp/HWxeUU5Y1xME62/XJemso1REREROS4pXIGuQ/4B3d/yszKgSfN7H/dfWPCMa8FFoeXs4Hbw3/HRE/U+fH2Fm5/ppGdLb0sqirk/718Om9YWE5+5CRLGSKR5BttqERCREREJKulLCC7+35gf/hxq5nVA7OBxID8JuDb7u7An8ysysxmhvc9YV19MX6wpYWvPdvIvvY+Tp1cxB0XzuTV8yYROZEAO7REorg42JJZRERERHLOuNQgm9l84HTg8SE3zQb2JHy+N7xuUEA2s2uBawHmzp497PO09cb4bn0TX9/QxOHOKGumFfPZtdO4oLYUG00wNkveRUIlEiIiIiITRsoDspmVAf8NfNjdW4benOQuftQV7ncCdwKsWbnyqNubuqPcs7GJuzc00dwT42WzSrnhgmrOnlEyfDAeWiIR32hDJRIiIiIiE1pKA7KZFRCE43vd/f4kh+wF5iR8XgvsG+kxeyN5vFg1jcmdzRxpaufrzzXx3fom2vucV82dxAdW1bBqavHgO+XnH91OTSUSIiIiIpJEKrtYGPANoN7dvzTMYT8FPmBm3ydYnNd8rPrjTQfbuOTup/jy21bxhUf38uTzTbx+QRnXr6xh2eRilUiIiIiIyElJ5QzyecC7gGfNbF143ceAuQDufgfwC4IWb9sI2rxdPZoH3tvYyd/+cD03X7aSyb0dLJhZNdBbWCUSIiIiInISUtnF4hGS1xgnHuPADSfy+HsbO5lZXcrs6ikncncRERERkaRSuH1catVWl1CYr9IJERERERlbWRmQa6tLuOvKNUyepO2aRURERGRsjUsf5LG0bEY5P7r+PCZPKiRysrvhiYiIiIgMkXUBuSAv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",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 6. Calculate the standard deviation and variance of the Sum of Encounter Count by Fiscal Year. \n",
    "encounters_by_fiscal_year_stats['Standard Deviation'] = encounters_by_fiscal_year_stats['Encounter Count'].std()\n",
    "encounters_by_fiscal_year_stats['Variance'] = encounters_by_fiscal_year_stats['Encounter Count'].var()\n",
    "# Display the updated DataFrame with standard deviation and variance\n",
    "print(encounters_by_fiscal_year_stats[['Fiscal Year', 'Encounter Count', 'Mean', 'Median', 'Standard Deviation', 'Variance']])\n",
    "# 7. Create a line plot of the Sum of Encounter Count by Fiscal Year with a trend line. Add title and labels. Use seaborn for styling.\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.lineplot(data=encounters_by_fiscal_year_stats, x='Fiscal Year', y='Encounter Count', marker='o', label='Total Encounters')\n",
    "sns.regplot(data=encounters_by_fiscal_year_stats, x='Fiscal Year', y='Encounter Count', scatter=False, color='red', label='Trend Line')\n",
    "plt.title('Total Encounters by Fiscal Year with Trend Line')\n",
    "plt.xlabel('Fiscal Year')\n",
    "plt.ylabel('Total Encounters')\n",
    "plt.xticks(rotation=45)\n",
    "plt.legend()\n",
    "plt.tight_layout()\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "52406795",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "hovertemplate": "Fiscal Year=%{x}<br>Total Encounters=%{text}<extra></extra>",
         "legendgroup": "",
         "marker": {
          "color": "#636efa",
          "pattern": {
           "shape": ""
          }
         },
         "name": "",
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "text": [
          1956519,
          2766582,
          3201144,
          2901142
         ],
         "textposition": "auto",
         "type": "bar",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          1956519,
          2766582,
          3201144,
          2901142
         ],
         "yaxis": "y"
        },
        {
         "line": {
          "color": "green",
          "dash": "dash"
         },
         "mode": "lines+markers",
         "name": "Max",
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "y": [
          3201144,
          3201144,
          3201144,
          3201144
         ]
        },
        {
         "line": {
          "color": "brown",
          "dash": "dash"
         },
         "mode": "lines+markers",
         "name": "Min",
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "y": [
          1956519,
          1956519,
          1956519,
          1956519
         ]
        }
       ],
       "layout": {
        "barmode": "relative",
        "legend": {
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Total Encounters by Fiscal Year with Max and Min"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Fiscal Year"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Total Encounters"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 7. Max and Min of the Sum of Encounter Count by Fiscal Year. Add interactive table with plotly. Add max and min results to the table.\n",
    "encounters_by_fiscal_year_stats['Max'] = encounters_by_fiscal_year_stats['Encounter Count'].max()\n",
    "encounters_by_fiscal_year_stats['Min'] = encounters_by_fiscal_year_stats['Encounter Count'].min()\n",
    "fig = px.bar(encounters_by_fiscal_year_stats, x='Fiscal Year', y='Encounter Count',\n",
    "             title='Total Encounters by Fiscal Year with Max and Min',\n",
    "             labels={'Encounter Count': 'Total Encounters'},\n",
    "             text='Encounter Count')\n",
    "fig.add_scatter(x=encounters_by_fiscal_year_stats['Fiscal Year'], y=encounters_by_fiscal_year_stats['Max'],\n",
    "                mode='lines+markers', name='Max', line=dict(color='green', dash='dash'))\n",
    "fig.add_scatter(x=encounters_by_fiscal_year_stats['Fiscal Year'], y=encounters_by_fiscal_year_stats['Min'],\n",
    "                mode='lines+markers', name='Min', line=dict(color='brown', dash='dash'))\n",
    "fig.update_layout(yaxis_title='Total Encounters', xaxis_title='Fiscal Year')\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "c158800c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "hovertemplate": "Fiscal Year=%{x}<br>Total Encounters=%{text}<extra></extra>",
         "legendgroup": "",
         "marker": {
          "color": "#636efa",
          "pattern": {
           "shape": ""
          }
         },
         "name": "",
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "text": [
          1956519,
          2766582,
          3201144,
          2901142
         ],
         "textposition": "auto",
         "type": "bar",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          1956519,
          2766582,
          3201144,
          2901142
         ],
         "yaxis": "y"
        },
        {
         "line": {
          "dash": "dash"
         },
         "mode": "lines+markers",
         "name": "Percentile 25",
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "y": [
          2564066.25,
          2564066.25,
          2564066.25,
          2564066.25
         ]
        },
        {
         "line": {
          "dash": "dash"
         },
         "mode": "lines+markers",
         "name": "Percentile 50",
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "y": [
          2833862,
          2833862,
          2833862,
          2833862
         ]
        },
        {
         "line": {
          "dash": "dash"
         },
         "mode": "lines+markers",
         "name": "Percentile 75",
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "y": [
          2976142.5,
          2976142.5,
          2976142.5,
          2976142.5
         ]
        },
        {
         "line": {
          "dash": "dash"
         },
         "mode": "lines+markers",
         "name": "Percentile 90",
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "y": [
          3111143.4,
          3111143.4,
          3111143.4,
          3111143.4
         ]
        },
        {
         "line": {
          "dash": "dash"
         },
         "mode": "lines+markers",
         "name": "Percentile 95",
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "y": [
          3156143.6999999997,
          3156143.6999999997,
          3156143.6999999997,
          3156143.6999999997
         ]
        }
       ],
       "layout": {
        "barmode": "relative",
        "legend": {
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Total Encounters by Fiscal Year with Percentiles"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Fiscal Year"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Total Encounters"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 8. Display percentiles of the Sum of Encounter Count by Fiscal Year. Add interactive table with plotly. Add percentile results to the table.\n",
    "percentiles = [0.25, 0.5, 0.75, 0.9, 0.95]\n",
    "for p in percentiles:\n",
    "    encounters_by_fiscal_year_stats[f'Percentile {int(p*100)}'] = encounters_by_fiscal_year_stats['Encounter Count'].quantile(p)\n",
    "fig = px.bar(encounters_by_fiscal_year_stats, x='Fiscal Year', y='Encounter Count',\n",
    "             title='Total Encounters by Fiscal Year with Percentiles',\n",
    "             labels={'Encounter Count': 'Total Encounters'},\n",
    "             text='Encounter Count')\n",
    "for p in percentiles:\n",
    "    fig.add_scatter(x=encounters_by_fiscal_year_stats['Fiscal Year'], y=encounters_by_fiscal_year_stats[f'Percentile {int(p*100)}'],\n",
    "                    mode='lines+markers', name=f'Percentile {int(p*100)}', line=dict(dash='dash'))\n",
    "fig.update_layout(yaxis_title='Total Encounters', xaxis_title='Fiscal Year')\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "9043fd7f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "Fiscal Year=%{x}<br>Total Encounters=%{text}<extra></extra>",
         "legendgroup": "",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "text+markers+lines",
         "name": "",
         "orientation": "v",
         "showlegend": false,
         "text": [
          1956519,
          2766582,
          3201144,
          2901142
         ],
         "textposition": "top center",
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          1956519,
          2766582,
          3201144,
          2901142
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "legend": {
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Yearly Trend of Total Encounters"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Fiscal Year FY21-FY24"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Total Encounters"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 9. Create a yearly trend line for the Sum of Encounter Count by Fiscal Year. Add interactive table with plotly. Add trend line to the table.\n",
    "fig = px.line(encounters_by_fiscal_year_stats, x='Fiscal Year', y='Encounter Count',\n",
    "              title='Yearly Trend of Total Encounters',\n",
    "              labels={'Encounter Count': 'Total Encounters'},\n",
    "              text='Encounter Count')\n",
    "fig.update_traces(textposition='top center')\n",
    "fig.update_layout(yaxis_title='Total Encounters', xaxis_title='Fiscal Year FY21-FY24')\n",
    "fig.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "41c1d647",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAyMAAAI4CAYAAAB5tTYpAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAB2IUlEQVR4nO3dd3gUVdvH8e+dRu9FuqCCDRERsAvYwALWR1FRsWHDAj4q9v7asTfsDdujWLEixS5VEQVFivTee5L7/WOGsAkBFtjJbpLf57rmyk49ZyaTzd57n3PG3B0REREREZGilpbsCoiIiIiISOmkYERERERERJJCwYiIiIiIiCSFghEREREREUkKBSMiIiIiIpIUCkZERERERCQpFIyIFHNm5ma2S7LrUdyYWXszm57sehR3W7qOZvaMmd1clHUqpA63mdnrW7nPmWb2ZYR1etnM7orq+CIixYWCEZGImNnymCnXzFbFzJ+5iX0S+gHZzIaY2eoCdfk4UcdPtOL6AS2s91ozWxZOv5vZPWZWJdl1SzZ3v9jd70x2PTYl/JvLLfg34u5vuPtRSajPnma2xMyaFVg+yMzuKer6iIhETcGISETcveL6CfgX6Byz7I0irErP2Lq4e+ciLLtImVlGEou/390rAbWAc4H9ge/NrEIS67RFSb5mqWJmqvyNuPs44EHgBTMzADM7H6gP3J6IMiyg//8ikhL0ZiRSxMysjJk9YmYzw+mRcFkF4DOgXsw3tPXMrK2Z/Whmi81slpk9YWZZCahHezObbmZXm9nc8NjnxqwvZ2YPmdnU8Jva78ysXLiui5mNC+s0xMx2j9kvX7Ox2GzH5so0sx7AmcC1sRmc8Bq8Z2bzzGyymV0Rc+zbzOx/Zva6mS0FuofXa4SZLTWzOWbWdwvX4QYzm29mU9ZnrMysTbhvRsx2J5vZmC1dV3df7e7DgS5ADYLAZP0xzjOzP81skZl9YWY7Frhul5rZ32F25U4z2zn83S81s3dif+9mdqGZTTSzhWb2kZnVi1l3lJlNCH9vT5nZUDO7IFzX3cy+N7OHzWwhcFtYzjdmtiC8Fm+YWdWY400xs+vN7I+w7i+ZWdkC13FT91G+bJeZHW9mY8Jz+sfMOm3i99InXL8sLPfEmHXdw/vxwbA+k83s6Jj1TcJzXmZmXwE1t/R7K6T87mb2Xfjawus1N7ymv5lZ83Dd5v5O3jWz2eHyYWa2Z5zF3wNUBC41sx2A+4DzAA/P+d/w/nwmpqxqZvZJ+HeyKHzdIOZ8hpjZ3Wb2PbAS2Glrr4mISBQUjIgUvRsJvjVvCewNtAVucvcVwNHk/5Z2JpAD9CL4QHUAcDhwaYLqUgeoQvCt6/nAk2ZWLVz3ILAvcCBQHbgWyLWg+cibwFUEWYCBwMcWf4BUaJnu3g94gyDDUNHdO1vw7e3HwK/h9ocDV5lZx5jjHQ/8D6ga7v8o8Ki7VwZ2Bt7ZQl1qhsc+B+hnZruGwcQC4MiYbbsBr8V5jrj7MuAr4BAAMzsBuAE4ieC6fUtwHWN1Irjm+xNc734EAVpDoDlweniswwg+sJ4K1AWmAm+F62qG1+N6gmBoAsHvMNZ+wCSgNnA3YOHx6gG7h+XdVmCfM4GOBNe0GXBTzLrN3Ud5zKwt8CpwDcHv61BgSsHtQv8QXLsqBBmB182sboFzmEDw+7ufmEwC0B8YGa67k+B3uz2OCuvaLKz3aQT3B2zi7yRc9xnQlOA6jyK4P7fI3bMJgo87gdeB1939B4KgpBnBe8cuBNf7lnC3NOAlYEegEbAKeKLAoc8CegCVCO4ZEZHkc3dNmjRFPBF84DoifP0PcEzMuo7AlPB1e2D6Fo51FTAgZt6BXTax7RCCb0EXx0x3xpS1CsiI2X4uwQfhtHDd3oUc82bgnZj5NGAG0L6w+gAvA3dtqcyC24bz+wH/Fij/euCl8PVtwLAC64cRfHituYXr2B7IBirELHsHuDl8fR3wRvi6engd627iWPnqHbP8XuCr8PVnwPkFrttKYMeY63ZQzPqRwHUx8w8Bj4SvXyAI2tavqwisAxoDZwM/xqwzYBpwQTjfveA1LaTeJwCjC9y/F8fMHwP8s7W/U+BZ4OFt/BsaAxwfcw4TY9aVD69fHYIP4gV/r/0JPtBv6j7IJf/fyKlhGd+F2xwG/EX4t1Hgd1jo30kh5VQN61hlc/dMgX0eAKaH52fACmDnmPUHAJM3sW9LYFHM/BDgjm259po0aUrsBLwYvk/+Huf2pwJ/AOOA/smuf6InZUZEil498n8rOTVcVigzaxY2uZhtQVOk/2Prmp1c4e5VY6bYkY0WePAt7HorCT7Y1gTKEgROm62/u+cSfNitH2d9NlVmYXYkaLa2eP1EkF3YIWabaQX2OZ/g2+PxZjbczI7bTF0WeZCRWi/2d/E60NnMKhL8I/jW3Wdt7sQKUR9YGHMuj8acx0KCD5ix121OzOtVhcyvv04FfwfLCb6prx+umxazzgk+0MbKd83MrLaZvWVmM8J77HU2vsdi9yl4z8b7O21I4ffURszs7LA51/rr1bxAnWavf+HuK8OXFcN6FfZ73ZyZBf5G8mXT3P0bgizDk8AcM+tnZpXZzN+JmaWb2b1hU7OlbMgAbc3f7jiCLypWEmTTygMjY67J5+FyzKy8mT0bNhdbShCUVzWz9JjjFfxbEZHkeJkgE75FZtaU4Eu4g9x9T4IvJEsUBSMiRW8mwQfT9RqFyyD45rSgp4HxQFMPmh7dQPAhNkrzgdUETXIKylf/sGlMQ4LsCAQfRMvHbF9nK8oteP7TCL75jf2gWMndj9nUPu7+t7ufTtA05j7gf7bpTuTVCqzL+124+wzgR+BEguYtcTfRAgiDmCMImmOtP5eLCpxLOQ+a32ytgr+DCgRNsmYAs4DYvgIWOx8qeJ3vCZe1CO+xbmx8jzWMeR17z26NaRR+T+VjQV+a54CeQA13rwr8XkidCjOLwn+v28XdH3P3fYE9CYLda9j838kZBE0IjyBoatY4XL6tf7vzCQLSPWPunyoeDJABcDWwK7Bf+Ds8tJDyCnt/EZEi5u7D2PBFFQAW9N373MxGmtm3ZrZbuOpC4El3XxTuO7eIqxs5BSMiRe9N4CYzqxW277+F4JtoCL4Jr2H5h4StBCwFlodvTpdEXcEw2/Ei0NeCDuTpZnaAmZUhaMp0rJkdbmaZBB+C1gDrP1SPAc4I9+kEtNuKoueQv2PtL8BSM7su7CicbmbNzazNpg5gZt3MrFZ4DovDxTmbKfN2M8sys0OA44B3Y9a9StAHYC9gQDwnYMFgBPsCHwCLCNrxAzwDXL++E7OZVTGz/8RzzEL0B841s5bh7+T/gJ/dfQrwKbCXmZ1gQQf8y9hyQFgJWA4sNrP6BB+0C7rMzBqYWXWCgPjtbaj3C2G9DzezNDOrH/MPN1YFgg/O8wAs6BDfPJ4C3H0qMIINv9eDge0aHcuCAQ32C+/3FQQBSM4W/k4qEfxdLCAIzv9ve+oQlvUc8LCZ1Q7rVT+m/1QlgmBlcfg7unV7yhORItcPuDz80uO/wFPh8mZAMwsGHvnJNjHoR3GmYESk6N1F8GHpN2AsQcfWuwDcfTxBsDIpbIpRj+BN6QxgGcGHka39EPiE5X+Gwsg49/tvWL/hBN/g3EfQXn4CwTfnjxN8W9uZYNjiteF+V4bLFhN0ev5gK+r6ArBHeO4fuHtOeKyWwOSwvOcJvmnelE7AODNbTtCZvau7r97EtrMJAoaZBJ2LLw5/B+sNIMhADCjQ7Kcw15rZMoJr9SpBn48D1+/n7gMIruFbYTOa3wkGLNhq7j6IoO/OewSZgJ2BruG6+cB/CDp1LwD2ILjf1mzmkLcDrYAlBMHM+4Vs0x/4kqDj+yTCe3Yr6/0LwehiD4dlDSV/lnD9dn8Q9JH5kSBA3Qv4fiuKOoOgv9FCgg/lr25tXQuoTPC3t4igydcCgo7rsIm/k7DMqQTZqj+An7azDhD0Y5oI/BTeQ18TZEMAHgHKEfyN/ETQhEtEioEwk34g8K4FozY+SzA4CUAGwUAY7QkGMXneYkY7LAks7BgjIiKFMLN/CJpXfZ3sumwLC0Ykmw6c6e6Dt/EYUwg6wBfLayAikmrMrDHwibs3D/ugTXD3uoVs9wzwk7u/HM4PAvp4MOpjiaDMiIjIJpjZyQTNhb5Jdl22hpl1NLOqYXOh9X2MEvHNvIiIJJi7LwUmr2+6a4G9w9UfAB3C5TUJmm1NSkY9o6JgRESkEGY2hGDwgMvC9vrFyQEEIzytb0Z3gruvSm6VREQEwMzeJGiGuqsFDwI+n6BZ8/lm9ivBSHrHh5t/ASwwsz+AwcA17r6gsOMWV2qmJSIiIiIiSaHMiIiIiIiIJEVGsiuwKUem/UcpGxERERHJ56vcd6N+1tZ2y53dLPLPsWl1/kr56xAPZUZERERERCQpFIyIiIiIiEhSpGwzLRERERGR4iiX6AdhLCkZhZJyHiIiIiIiUswoMyIiIiIikkA5RfB4qpLyIV6ZERERERERSYqSElSJiIiIiKSEXPSEingpMyIiIiIiIkmhzIiIiIiISAIVxWhaJYUyIyIiIiIikhTKjIiIiIiIJFCOq89IvJQZERERERFJoFw88mlzzKyhmQ02sz/NbJyZXVnINmZmj5nZRDP7zcxaxazrZGYTwnV9IrhEeRSMiIiIiIiULNnA1e6+O7A/cJmZ7VFgm6OBpuHUA3gawMzSgSfD9XsApxeyb8KomZaIiIiISALlJHloX3efBcwKXy8zsz+B+sAfMZsdD7zq7g78ZGZVzawu0BiY6O6TAMzsrXDb2H0TRpkREREREZFixsx6mNmImKnHJrZrDOwD/FxgVX1gWsz89HDZppZHQpkREREREZEEKoqHHrp7P6Df5rYxs4rAe8BV7r604OrCDruZ5ZFQMCIiIiIiUsKYWSZBIPKGu79fyCbTgYYx8w2AmUDWJpZHQsGIiIiIiEgCJXtoXzMz4AXgT3fvu4nNPgJ6hn1C9gOWuPssM5sHNDWzJsAMoCtwRlR1VTAiIiIiIlKyHAScBYw1szHhshuARgDu/gwwEDgGmAisBM4N12WbWU/gCyAdeNHdx0VVUQUjIiIiIiIJlJvk8t39Owrv+xG7jQOXbWLdQIJgJXIaTUtERERERJJCmRERERERkQRK9nNGihNlRkREREREJCmUGRERERERSaAcJUbipsyIiIiIiIgkhTIjIiIiIiIJlOzRtIoTZUZERERERCQplBkREREREUmgnM0/4kNiKDMiIiIiIiJJocyIiIiIiEgC5Wo0rbgpMyIiIiIiIkmhzIiIiIiISAKpz0j8lBkREREREZGkUGZERERERCSBlBmJnzIjIiIiIiKSFMqMiIiIiIgkUK4rMxIvBSMiIiIiIgmkZlrxUzMtERERERFJCmVGREREREQSKEff98dNV0pERERERJJCmRERERERkQRSB/b4KTMiIiIiIiJJocyIiIiIiEgCaTSt+CkzIiIiIiIiSaHMiIiIiIhIAuW4vu+Pl66UiIiIiIgkhTIjIiIiIiIJlKvv++OmKyUiIiIiIkmhzIiIiIiISAJpNK34KTMiIiIiIiJJocyIiIiIiEgCaTSt+OlKiYiIiIhIUigzIiIiIiKSQLnqMxI3ZUZERERERCQplBkREREREUmgHH3fHzddKRERERERSQplRkREREREEkijacVPwUgxklkmk75D7yCzTAbpGel8+95PvHrbO1SqVpEb3+pFnca1mD1lHned1pfli1fQ6ogWnH/PmWRmZbBubTbPXfsaYwb/nu+Yd3xwHXV2qk2PFlcn6aykuHpt0pOsWraa3JxccrJzuKxtH3ZqsSNXPt2DchXLMnvKXO7t9hgrl60iPSOd3s9dTNNWO5GekcZXrw3lrXs/AODBb26jet1qrF21FoA+He9k8bylSTwzKS4aNKvHTW/1ypuvs1NtXrn1bQY8OhCAU67uzEUPnM3Jtc5j6YJlm7wPy5TL4uZ3rqbuzjuQm5PLT5+M5IXr30jWaUkxtDXvhwBd+5xAp/MOJzcnl6eufJERX/4KQEZmBj2fOJ+92+1Bbq7z0k1v8t37Pyfz1EQip2CkGFm3Zh3XHH47q1esJj0jnYe/vZPhn43moJP2Y/Q3Y3n7vg847boT6NrnBJ7v8wZL5i/lli73smDWIhrv2ZB7Pr+J0xtelHe8g09sy6rlq5N4RlLc/few21i6YFnefO/nLqbfNa/x27A/6HhuB/5zTRdeueVtDv3PAWSWyaTH3ldTplwWz497mMFvfs+cqfMAuLfbo/w1clKSzkKKq+l/zeTiVtcAkJaWxpvTn+X7Ab8AUKtBDfY9okXePQZs8j5cPHcJ7z70Eb8OGUdGZgb3f30LbTq1ZPjnY5JxWlJMxft+2Gj3BrQ/7SAubN6LGvWqc99XN3PurleSm5vLGTeexOK5Szh3tysxMypVr5i8E5LtkqueEHGL7EqZWQUzSwtfNzOzLmaWGVV5pcXqFUHwkJGZTkZmOu7OgV3a8NUrQwD46pUhHHh8WwD+GTOFBbMWATBl3DSyymaSmRXEn2UrlOXkXp154+73iv4kpMRqsGs9fhv2BwCjvvqNQ07aP1jhTtkKZUhLTyOrXBbZa7NZuXRVEmsqJc0+hzdn1j+zmfvvfAAu7tud5657HXffsNEm7sM1q9by65BxAGSvy2bi6MnUbFAjGachJcim3g8PPL41Q97+nnVrs5k9ZS4zJ85m17a7ANDx3A68dc8AANw9X3AjUlJFGbYNA8qaWX1gEHAu8HKE5ZUKaWlpPDPqAd6d8wKjvv6N8b9MpNoOVVg4ezEAC2cvpmrtyhvtd8jJ+zNx9GTWrc0GoPudp/G/vh+zZuWaoqy+lCDucO8XN/Hk8Ps45sIjAJjy+zQO6NIaCL6FrtUw+EA37H8/sXrFGt6e+RxvTH2adx/6mGWLlucd678vXsYzox7gzJtOLvoTkRKhfdeDGPzW9wAc0Lk1C2YuZNJvU/Nts6X7EKBClfLsf9y+jB40tsjqLsXf1rwf1qxfg3nTFuTtO2/GQmrWr06FKuUBOOfOrjw14j5ufrs3VWtXKeIzkUTJcYt8KimiDEbM3VcCJwGPu/uJwB6b3cGsh5mNMLMR011NNgqTm5vLxa2u4fSGF7Frm11ovGfDLe6z4x4NuODeM3nk4n4A7Lx3Y+rtXIfvP/gl6upKCdbr4Ju4tPV13HjM3XS5tCN7HbI7D53/FMdf2oknh99HuUplyQ6D393a7kJuTi5d6/fg7J0u45TenanTpDYA93R7jB57X02vQ29mr4N354izDk3maUkxlJGZwQGdWzP03R8pUy6L0284iZdveXuj7TZ3HwKkpadxQ/+rGPD4QGZPnluUpyDF3Na8H1ohnyHdnfSMdGo3rMm478dzaevr+OOnv7jogbOL+EwkUXJIi3wqKSINRszsAOBM4NNw2Wb7qLh7P3dv7e6tG9hOEVat+FuxZCW/Dh1H604tWTRnCdXrVAWgep2qLJ67ofNvzfrVue39a7j/nCeYNWkOALsf0Ixm++7Ea5Oe5OFv76RBs3o8+M1tSTgLKc7WNwFcPG8p33/wC7u23YVpE2bSp9NdXNbmOga/+T0z/wnuucPOOJgRX4whJzuHxfOWMu6H8TRrvXNwnJkLAVi1fDXfvPkdu7VtmpwTkmKrzdEtmThqMovnLqHuznWo06Q2z455gNcmPUmtBjV4euT9VNuh6mbvQ4Be/S5ixsRZeR3gReK1Ne+H86YvyMuSANSqX50FMxexdMEyVq1Yndfvadi7P7JLqyZFfzIiRSzKYORK4HpggLuPM7OdgMERllfiValZOS+Nm1U2i1aHt2Da+Bn8+PEIjjynPQBHntOeHz4aDgTNDe765HpeuKE/436YkHecT575kq4NLuKsnS6j1yE3M/2vmfz3sNuK+GykOCtbvgzlKpbNe73vkXsz5fdpVK0VNBE0M8688WQ+efZLAOb+O5+WHZrnbb/7fs2YNn4GaelpVK5RCYD0jHT2O3Zfpvz+bxLOSIqzDl0PZvBb3wEw5fd/ObXOBZy102WctdNlzJu+gEv2vZZFcxZv8j4E6H5nVypULs/TV72crNOQYmpr3w9//GgE7U87iMysDOo0rk39pnWZ8MtEAH76eCR7t98TgH0O34t//5iehDOSRMj1tMinkiKS0bTMLB3o7O5d1i9z90nAFVGUV1pUr1uVa1/uSVp6GpZmDHv3R37+dBR//PgXN7/dm6PPO4y5/87nzlP7AnB8z07U26UO3W46hW43nQJo2FRJjKo7VOG294NRjNIz0hn85neM+GIMJ15xDF0u7QjAdwN+4YuXgu8fPnzyC6558VKeG9sXM+OLlwczeey/lC1fhns+v4mMzHTS0tMYPWgsA58blLTzkuKnTLks9j2yRV4z1M3Z1H1Ys351zrzxZP79czpPj7w/3PYzPnvhm6irLyXA1r4fTv1jOsPe/ZHnxz1MTnYuj/d8ntzcXACe7/M61716OZc83J0l85bywHlPJeekRIqQ5RtpJJEHNvvG3Q/b1v2PTPtPNBUTERERkWLrq9x3U773dv+J+0X+OfaMXX5O+esQjyifMzLazD4C3gVWrF/o7u9HWKaIiIiIiBQTUQYj1YEFQGx2xAEFIyIiIiJSYpWkoXejFlkw4u7nRnVsEREREREp/qJ8AnsDMxtgZnPNbI6ZvWdmDaIqT0REREQkFeSSFvlUUkR5Ji8BHwH1gPrAx+EyERERERGRSPuM1HL32ODjZTO7KsLyRERERESSLicFngNiZi8CxwFz3b15IeuvIXg4OQQxwe4En98XmtkUYBmQA2S7e+uo6hnllZpvZt3MLD2cuhF0aBcRERERkWi9DHTa1Ep3f8DdW7p7S4IHlQ9194Uxm3QI10cWiEC0wch5wKnAbGAWcEq4TERERESkxMrFIp+2xN2HAQu3uGHgdODN7TnnbRXlaFr/Al22uKGIiIiIiGwVM+sB9IhZ1M/d+23DccoTZFB6xix24Eszc+DZbTluvCILRsysFnAh0Di2HHdXdkRERERESqyi6DMSBgiJCBI6A98XaKJ1kLvPNLPawFdmNj7MtCRclB3YPwS+Bb4m6PwiIiIiIiKppSsFmmi5+8zw51wzGwC0BYpdMFLe3a+L8PgiIiIiIiknp5g8B8TMqgDtgG4xyyoAae6+LHx9FHBHVHWIMhj5xMyOcfeBEZYhIiIiIiIFmNmbQHugpplNB24FMgHc/ZlwsxOBL919RcyuOwADzAyCWKG/u38eVT2jDEauBG4wszXAOsAAd/fKEZYpIiIiIpJUub7l0a6i5u6nx7HNywRDAMcumwTsHU2tNhblaFqVojq2iIiIiIgUfwkPRsxsN3cfb2atClvv7qMSXaaIiIiISKooLn1GUkEUmZGrCYb0faiQdQ4cFkGZIiIiIiJSzCQ8GHH3C8OfHRJ9bBERERGRVJdbBM8ZKSmiaKZ10ubWu/v7iS5TRERERESKnyiaaf0PGBNOEIyitZ4DCkZEREREpMTKIfmjaRUXUQQjJwOnAS0InsL+prtPjKAcEREREZGUo2Za8Uv4lXL3Ae7eleBpjv8AD5nZd2bWLtFliYiIiIhI8RXlQw9XA0uApUAjoGyEZYmIiIiIpAQ104pfFB3YOwCnA22Br4FH3X1EossREREREZHiLYrMyCDgN+A7oAxwtpmdvX6lu18RQZkiIiIiIilBfUbiF0Uwcm4ExxQRERERkRImiocevpLoY4qIiIiIFBc5yozETVdKRERERESSIsrRtERERERESp1cjaYVN2VGREREREQkKaIY2vdxwDe1XqNpiYiIiEhJpj4j8YviSo0ARhI85LAV8Hc4tQRyIihPRERERESKochG0zKz7kAHd18Xzj8DfJno8kREREREUkmuq89IvKLMIdUDKsXMVwyXiYiIiIiIRDqa1r3AaDMbHM63A26LsDwRERERkaTL0RhRcYssGHH3l8zsM2C/cFEfd58dVXkiIiIiIlK8RBa2mZkBRwB7u/uHQJaZtY2qPBERERGRVJDrFvlUUkSZQ3oKOAA4PZxfBjwZYXkiIiIiIlKMRNlnZD93b2VmowHcfZGZZUVYnoiIiIhI0uWqz0jcorxS68wsnfABiGZWC8iNsDwRERERESlGosyMPAYMAGqb2d3AKcBNEZYnIiIiIpJ0OSWoT0fUohxN6w0zGwkcDhhwgrv/GVV5IiIiIiJSvCQ8GDGzyu6+1MyqA3OBN2PWVXf3hYkuU0REREQkVZSk0a6iFkVmpD9wHDCSoL+IFfi5UwRlioiIiIhIMZPwYMTdjwt/Nkn0sUVEREREUl2uazSteEXZgR0zqw/sGFuOuw+LskwRERERkWTKQc204hVZMGJm9wGnAX8AOeFiBxSMiIiIiIhIpJmRE4Bd3X1NhGWIiIiIiKQUdWCPX5QN2iYBmREeX0REREREirEoMyMrgTFmNgjIy464+xURlikiIiIiklTqwB6/KIORj8JJRERERERkI1E+gf2VqI4tIiIiIpKqcjWaVtyiHE2rKXAPsAdQdv1yd9dDD0VEREREJNJmWi8BtwIPAx2Ac0FhooiIiIiUbDkaTStuUfauKefugwBz96nufhtwWITliYiIiIhIMRJlZmS1maUBf5tZT2AGUDvC8kREREREkk6jacUvymDkKqA8cAVwJ0FW5Jx4d15zXNtoaiWyFVZXS092FURY0CLZNRAREYlGlKNpDQcIsyNXuPuyqMoSEREREUkVegJ7/CLLIZlZazMbC/wGjDWzX81s36jKExERERGR4iXKZlovApe6+7cAZnYwwQhbanAgIiIiIiWWnjMSvyh71yxbH4gAuPt3gJpqiYiIiIgIEG1m5BczexZ4E3DgNGCImbUCcPdREZYtIiIiIpIU6jMSvyiDkZbhz1sLLD+QIDjRM0dEREREREqxKEfT6hDVsUVEREREUpWeMxK/yIIRM6sKnA00ji3H3a+IqkwRERERESk+ogzbBhIEImOBkTGTiIiIiEiJlesW+bQlZvaimc01s983sb69mS0xszHhdEvMuk5mNsHMJppZnwRemo1E2WekrLv3jvD4IiIiIiJSuJeBJ4BXN7PNt+5+XOwCM0sHngSOBKYDw83sI3f/I4pKRhmMvGZmFwKfAGvWL3T3hRGWKSIiIiKSVKnwnBF3H2Zmjbdh17bARHefBGBmbwHHA5EEI1E201oLPAD8yIYmWiMiLE9EREREpFQwsx5mNiJm6rENhznAzH41s8/MbM9wWX1gWsw208NlkYgyM9Ib2MXd50dYhoiIiIhISimK54y4ez+g33YcYhSwo7svN7NjgA+AplBoWse3o5zNijIYGQesjPD4IiIiIiIppzg89NDdl8a8HmhmT5lZTYJMSMOYTRsAM6OqR5TBSA4wxswGk7/PiIb2FRERERFJIjOrA8xxdzeztgTdNxYAi4GmZtYEmAF0Bc6Iqh5RBiMfhJOIiIiISKmRCpkRM3sTaA/UNLPpwK1AJoC7PwOcAlxiZtnAKqCruzuQbWY9gS+AdOBFdx8XVT2jfAL7K2aWBTQLF01w93VRlSciIiIiIgF3P30L658gGPq3sHUDCZ4ZGLkon8DeHngFmELQEaahmZ3j7sOiKlNEREREJNlSITNSXETZTOsh4Ch3nwBgZs2AN4F9IyxTRERERESKiSiDkcz1gQiAu/9lZpkRliciIiIiknSp8NDD4iLKYGSEmb0AvBbOn0nw4EMREREREZFIg5FLgMuAKwj6jAwDnoqwPBERERGRpFOfkfhFGYxkAI+6e18AM0sHykRYnoiIiIiIFCNpER57EFAuZr4c8HWE5YmIiIiIJF2uW+RTSRFlMFLW3Zevnwlfl4+wPBERERERKUaibKa1wsxaufsoADPbl+DpjiIiIiIiJVZJylxELcpg5CrgXTObGc7XBU6LsDwRERERESlGIgtG3H24me0G7EowmtZ4d18XVXkiIiIiIqlAmZH4RdZnxMwuAyq4++/uPhaoaGaXRlWeiIiIiIgUL1F2YL/Q3Revn3H3RcCFEZYnIiIiIpJ07hb5VFJEGYykmVnelQqfM5IVYXkiIiIiIlKMRNmB/QvgHTN7BnDgYuDzCMsTEREREUm6XEpO5iJqUQYj1wE9gEsIOrB/CTwXYXkiIiIiIlKMRDmaVi7wTDhhZgcDjwOXRVWmiIiIiEiyaTSt+EWZGcHMWgKnEzxfZDLwfpTliYiIiIhI8ZHwYMTMmgFdCYKQBcDbgLl7h0SXJSIiIiKSakrSaFdRiyIzMh74Fujs7hMBzKxXBOWIiIiIiEgxFkUwcjJBZmSwmX0OvAUaUkBERERESgf1GYlfwoMRdx8ADDCzCsAJQC9gBzN7Ghjg7l8mukwRERERkVShZlrxi+yhh+6+wt3fcPfjgAbAGKBPVOWJiIiIiEjxEuloWuu5+0Lg2XASERERESmx1EwrfpFlRkRERERERDanSDIjIiIiIiKlhXuya1B8KDMiIiIiIiJJocyIiIiIiEgC5eqpFnFTZkRERERERJJCmRERERERkQTSc0bip8yIiIiIiIgkhTIjIiIiIiIJpOeMxE+ZERERERERSQplRkREREREEkjPGYmfMiMiIiIiIpIUyoyIiIiIiCSQRtOKnzIjIiIiIiKSFMqMiIiIiIgkkDIj8VNmREREREREkkKZERERERGRBNJzRuKnYCSFpaUZ/fqexfwFy+lz5/vs0qQ2V196JFmZGeTk5PLwM1/x59+z2b1pHf57WUcAzOClN3/g25/+BuDwQ3fjrFP2x4H5C5dz10OfsmTZqrwy2h3YjDv7HM+FvV9lwsQ5ANSuWYnrLu9E7ZqVcHeuveM9Zs9dWuTnL8lXsXwZbjzvSHauXxPHuev5L6ldvSIXnngAjevW4Nzb+/PnlDn59tmheiXevuccnvvgR974bCQAuzWuzS0XdKJMVgY//DqZh94YDMAZHVvRpd1e5OTmsnjpKu584QtmL1hGnRqVuO+KLqSbkZGRxjtfjeH9wb8V+flLaui+zz6c1mIvAN4eO5aXR41mt1o1ufOII6iQmcX0pUvoPfAzlq9dS4s6dbj7yCMAMIzHfvyRLydOBODYXZtx6X77kWbGkMmTuW/Yt/nK6dS0KU926cwJr7/B2Dlz2L9hQ25s3y5v/c7Vq3Plp5/y1cR/iujMJdVszb0IsGvNmtx15BFUzMrCHU544w3W5uTQvHZt7u/UibIZGQyZPJk7BgfviTe2b8f+DRsCUC4jkxrly7HPk0/llV8xK4svunfny4kTuf2bb4r47EWioWAkhZ3SeV+mTltAhfJlALikeztefvMHfh41mf33bcLF3dtx5Y1vM2nqfHr0fpWcXKdGtQq8+Og5/PBL8M/3igsO4+zLXmLJslVc3L0dJx23Dy+9+QMA5cplckrnVoybMDNfuTf2OobX3v2JEWOmUq5sJrm5Giy7tLr6zPb8NHYK1z/xCRnpaZQtk8mylWu49rGPub77EYXu0+uM9vz425R8y6475wjueekrxv4zi0euPpEDWjTmx9+mMGHqPM657Q3WrM3m5MNacPlph3LjU58yf/EKLrjzLdZl51CuTCZv3n02w0b/w/zFK4rgrCWVNKtRg9Na7MWJb/RnXU4OL518EkMmTeaeo47inqHD+GX6dE5pvicXtm7Nwz/8wF/z53PC62+Q406tChX49OyzGPTPP1QqU4Y+hx7K8a+/wcJVq3igU0cObNSQH/6dBkCFzEzOabUPo2fOyiv7p2nT6Pza6wBUKVuWb847j2+nTE3KdZDk29p7Md2MvscczdWffcb4efOpWrYs2bm5ANxxxBHc+NVXjJ41ixdPOpF2jRszdMoU7h4yNK+8s/dpyR61a+erQ6+DDuSX6dOL9Lxl2+g5I/Er0j4jZlbWzP5TlGUWV7VqVOSA1jvx6Vdj85a5OxXKZwFQoUIZ5i9cDsCatdnkhAFDVlYGefe/GWZG2bKZwT7lsvL2AbjgzIPp/94vrF2bnbdsx4Y1SE9PY8SY4B/uqtXrWBOzXkqPCmWz2GfXBnw49HcAsnNyWb5yDVNmLeTf2YsK3addq52ZMW8Jk2YsyFtWo0oFKpTNYuw/wYe8gd//QbtWuwAwcvy0vPtr7MRZ1K5eMa+sddk5AGRlpJOWpnR3abVzjeqMnjWL1dnZ5Ljzy/TpHNV0F5pUq5b3oez7qVPp2KwpQN52AGXS0/HwdcMqVZi8aBELV60K9/mXjk2b5pXT66CD6Dd8OGtyCn+/O7ppU4ZOmczqbL0fllZbey8e0rgx4+fNZ/y8+QAsXr2a3DBIrlgmi9GzgvfEAX/8wZG77LJReZ13242Px4/Pm29euzY1y5fnu6lTIj5TkaIVeTBiZulmdrSZvQpMBU6LusyS4PILDuPpl4fmy0o8/vw3XHJue/73wkVcem57+r26oYnB7s3q8soT5/LSY9156KmvyMl1cnJyeejpr3j58e4MePkSGjeqkRfcNN2pNrVrVubHEZPylduwXjWWr1jDXdcfz/OPnM0l3dvpg2ApVa92FRYtW8UtF3TktTu6ceN5R1I2a9PJ1LJZGZx9bBue/+DHfMtrV6vI3EXL8ubnLlxO7WoVN9q/S7u98mVUalevyBt3ncXHD1/Iq58OV1aklPpr/gLa1m9A1bJlKZuRQbsmTahbqRJ/L1jAETvvDMDRzZpRt1KlvH32rlOHz845m4HnnM3NXw8ix52pixezU/Xq1K9cmXQzjtxll7x99qhdi7qVKjF40uRN1uO43XbN98FQSp+tvRcbV6uK47x08kl82O1MerRpDUCdihWZvWzDe+KsZcvZoWL+98R6lSrRoHJlfgwzdwZc374d9w4bVgRnKongbpFPJUVkwYiZHWpmzwBTgAuAo4Am7n7KZvbpYWYjzGzErKk/RVW1lHdA651YtGQlf/2Tvy3+8Ue35InnB3PK+c/yxPODue7yTnnr/vxrFuf0fImLrn6NbqfsR1ZmOunpaZxwdEvOv+pVTuz+NP9MmUe3U/bDDHqe34EnXxy8Udnp6Wm02KMBT744hIt6v0a9OlU5+vDmkZ+zpJ6MtDR23bE2733zK2fd8jqr1qzjnOPabnL7HicdyJtfjGLVmnX5VxTyfukF8tedDtyd3RvvwGsDR+Qtm7twOWfe9BonXfsixx68J9Url9+u85Hi6Z+FC3l2+HBeOeVkXjr5JMbPm0d2bi7XffEF3VruzYfdzqRCVhbrcnLy9vl19myOfuVVTnyjPxe3bUtWejpL16zhlq8H8dhxx/JW19OYvnQJObmOATe2b8//DR26yTrUqlCBZjVrqolWKbe192JGWhqt69en98CBnPbW2xy5yy4c2Khhocd28r8nHrfbbnz+99/khu+V3Vq2ZOjkycxatryw3UWKtUj6jJjZdOBf4GngGndfZmaT3X3l5vZz935AP4BDuzxQalvb7bVHfQ5quwv777sTWVkZVCifxU29j+XANjvz2HNBh7XB30/g2ss7brTv1OkLWbV6HU12rImFnwJnzl4c7PPdBM48eT/Kl8uiyY41efTurgBUr1aBe248ievvfp95C5bx96Q5zJqzBIBvf/qbPXetx6eM3agsKdnmLlrG3IXLGDdpNgDfDP+bs49ts8ntm+9Uh8NaN6XnqYdQqXwZch3Wrsvhm+F/U7vahm+ta1evyLyYLEebPRpxbue2XPx/7+Q1zYo1f/EKJs2YT8tm9flmxN8JPEMpLt79/Xfe/T1oLnj1wQcxe9lyJi1cRPf33geCb6A7NNlpo/3+WbiQVevWsWvNmoydM4dvJk3im0lBNrjrXnuR606FrCya1axJ/1ODFsS1KlTg2ROO56IPPmTsnOALoWObNeOriRPz2vtL6bU19+LsZcv5Zdp0Fq1aDcDQyZPZs/YOfPDnn9SJyeTVrVSRucvzZ36P221Xbhs0KG9+n3p1aVO/PmfuvTfls7LITEtj5bq1PPDtd5Ger2y7kpS5iFpUHdjfA04gaJKVY2YfAqU2uNha/V79Nq8JVsvmDel6Yhvu6vsprz15Hi2bN2TM79No1aIR02cG7fbr7lCFufOWkpPr7FCrMo3qV2f2nKVkZKbRuGENqlQux5Klq2jdckemTl/AipVr6dLtybzyHr37NJ56aQgTJs4hLc2oVLFs3j6tWjTKG2VLSpcFS1Yyd+EyGtWpxr+zF9Fmj0ZMnrlwk9v3+L938l5feMIBrFyzlne/HgPAytVrab5zXX7/ZxbHHLQH73wVLG/WqBbXn3sEVz74PotiRnmrXa0iS5avZs26bCqVL8PeTevT//NRkZynpL4a5cqxYNUq6laqRMemTTml/5t5ywzoud/+9P/tVwAaVK7MrGXLyHGnXqVKNKlejelLl+Q7TuUyZTiz5d5c/sknLF+7ljZPPZ1X1hun/od7hw7LC0Qg+Jb6we/0oU+27l4cNmUKF7ZpTdmMDNbl5NC2QQNeHDmKeStWsGLtWlrWrcuYWbM4cY89eHX0mLwymlSrRpUyZRgVM5hC74Gf5b0+ec89aL5DHQUiKU4feuMXSTDi7lea2VVAB+B04AGgspmdCgx0d+UZt8H9T3zBFRceRnp6GmvXZvPAk18CsNfu9Tnz5pPIzs7F3en7zFd5w/e+9NYPPHHP6WTn5DJ77hLuefSzzRVBbq7z1EtDeOSu0zBgwj9z+PjLX6M+NUlRD7w+mDsvPpqMjHRmzl3CHc9/Qft9d+Hqbh2oVqkcfXufwN//zuOKB9/f7HHue2UQt1zYMRja97cp/PBb0Db/iq6HUq5MJvdcdhwAsxcu47+PfEjjetW58vR2wbu5weufjeCf6fOjPl1JUU926UzVcuXIzsnltkGDWLpmDd332YduLVsC8MXEv/nf7+MAaF2/Phe1bUN2bi657tw6aFDeN9M3H9aB3WrVAuCJH39iyqLFWyy7fuXK1K1UiZ+nTYvk3KR42Zp7cemaNbw4chQDzjwDgCGTJzNkcvDed8vXg7i/U0fKZGQwdPKUvOUQdFz/ZMKEoj0xkSSygm23IynELBM4GugKHOXuNbe0T2lupiWpY3W19GRXQYQFLZJdAxGR1PHP1b1Tvg1Us/fujPxz7F8n35zy1yEeRfKcEXdfB3wEfGRm5YqiTBERERERSW1RdWAfS/7mcg7MBwYDD0ZRpoiIiIhISkiB9j1m9iJwHDDX3TcaGtXMzgSuC2eXA5e4+6/huinAMiAHyHb31lHVM6rMyHGFLKsOnAM8DlwYUbkiIiIiIgIvA08Ar25i/WSgnbsvMrOjCUa03S9mfQd3j7zDZlQd2AsbjH0qMNrMRkdRpoiIiIhIKkiFoX3dfZiZNd7M+h9iZn8CGkReqUJE/gT2FClTREREREQKdz4QO+SqA1+a2Ugz6xFlwVH1GWlVyOJqQDdgWBRlioiIiIikgiIYrJYwSIgNFPqFDxDf2uN0IAhGDo5ZfJC7zzSz2sBXZjbe3SP5DB9Vn5GHCsw7sAAYQviEdRERERER2TZh4LFdn6vNrAXwPHC0uy+IOfbM8OdcMxsAtCWihEJUfUY6RHFcEREREZFUlwp9RrbEzBoB7wNnuftfMcsrAGnuvix8fRRwR1T1iKqZVu/NrXf3vlGUKyIiIiIiYGZvAu2BmmY2HbgVyARw92eAW4AawFNmBhuG8N0BGBAuywD6u/vnUdUzqmZaDwJjCDrCrAFSPzwUEREREUmEFMiMuPvpW1h/AXBBIcsnAXtHVa+CogpGWgFdgWOBkcCbwCD3oujOIyIiIiIixUEkw+y6+xh37+PuLYEXgOOBP8ysSxTliYiIiIikCvfop5Ii0md+mFktYB9gL2A6MDfK8kREREREpPiIqgP7ucBpQFngf8Cp7q5ARERERERKvhKUuYhaVH1GXgDGAv8CHYGjwh75ALi7mmuJiIiIiJRyUQUjes6IiIiIiJRKxeE5I6kiqmBksrv/G9GxRUREREQkBZjZf9z93S0t25SoOrB/EFOZ9yIqQ0REREQk9XgRTKnj+jiXFSqqzEhsbmqniMoQEREREZEkMLOjgWOA+mb2WMyqykB2vMeJKhjxTbwWERERESnRSkmfkZnACKALwUPO11sG9Ir3IFEFI3ub2VKCDEm58DXhvLt75YjKFRERERGRiLn7r8CvZtbf3ddt63EiCUbcPT2K44qIiIiIpLzS1S6orZndBuxIEFusTz7E1VUjqsyIiIiIiEgpVSqaaa33AkGzrJFAztburGBERERERES21RJ3/2xbd1YwIiIiIiKSSKWrmdZgM3sAeB9Ys36hu4+KZ2cFIyIiIiIisq32C3+2jlnmwGHx7BxXMGJmJwLfuPuScL4q0N7dP4i7miIiIiIipUEpyoy4e4ft2T/ezMit7j4gptDFZnYrMU9aFxERERGR0sXMbilsubvfEc/+8QYjaduxr4iIiIhI6VE6Hnq43oqY12WB44A/49053oBihJn1BZ4kSDxdTv4nLYqIiIiISCnj7g/FzpvZg8BH8e5fWMajMJcDa4G3gXeB1cBl8RYiIiIiIlJauEc/pbDyQFwPPIQ4MyPuvgLos601EhERERGRksfMxrKhy346UAuIq78IbCEYMbNH3P0qM/s4ppA87t5lK+oqIiIiIlLypXbmItGOi3mdDcxx9+x4d95SZuS18OeDW1srEREREREp2dx9qpntDRwSLhoG/Bbv/psNRtx9ZPhz6DbXUERERESkNClFo2mZ2ZXAhQRPYAd4w8z6ufvj8ewf70MPDwJuA3YM9zHA3T3uzikiIiIiIlLinA/sF/Yxx8zuA34EEheMAC8AvQiG883ZhkqKiIiIiJQKVrr6jBj544OccFlc4g1Glrj7Z1tTKxERERERKfFeAn42swHh/AkEiYy4bGk0rVbhy8Fm9gBBW7A169e7+6itqqqIiIiISElXijIj7t7XzIYABxNkRM5199Hx7r+lzMhDBeZbx5YNHBZvQSIiIiIiUjKYWRugprt/FiYoRoXLu5hZ2vqBsLZkS6Npddj+qoqIiIiIlCKlYzStB4DuhSz/A+hHnEmLtHg2MrMaZvaYmY0ys5Fm9qiZ1Yi7qiIiIiIiUpLUcPcpBRe6+0Qg7jghrmAEeAuYB5wMnBK+fjveQkRERERESg0vgin5ym1mXYV4DxJvMFLd3e9098nhdBdQNd5CRERERESkRPnazO42s3xt0szsduCbeA8S79C+g82sK/BOOH8K8Gm8hYiIiIiIlBqpkbmI2tXA88BEMxsTLtsbGAFcEO9B4g1GLgJ6A6+H82nACjPrTfAk9srxFigiIiIiIsVb+MT1081sJ2DPcPE4d5+0NceJKxhx90pbWT8RERERkdKpdGRGAAiDj60KQGLFmxnBzKoBTYGyMYUP29aCRURERERKpNIxtG9CxBWMmNkFwJVAA2AMsD/wI3rooYiIiIiIbKN4R9O6EmgDTA0fhLgPwfC+IiIiIiISwzz6KRWYWZqZ/b49x4g3GFnt7qvDQsu4+3hg1+0pWEREREREii93zwV+NbNG23qMePuMTDezqsAHwFdmtgiYua2FioiIiIiUWCmSuSgidYFxZvYLsGL9QnfvEs/O8Y6mdWL48jYzGwxUAT7fyoqKiIiIiEjJcvv27LzFYMTM0oDf3L05gLsP3Z4CRURERESkZHD3oWa2I9DU3b82s/JAerz7b7HPSCLagomIiIiISMljZhcC/wOeDRfVJ+jaEZd4+4xsV1swEREREZHSIlVGuyoilwFtgZ8B3P1vM6sd787xBiPb1RZsWyy6YHlRFymykW9aP5/sKohQI61CsqsgAsC7y6skuwoiQO9kV0DyW+Pua82CBz2aWQZb0YU/3g7s6iciIiIiIhKP0vUE9qFmdgNQzsyOBC4FPo5357ieM2Jmy8xsaYFpmpkNMLOdtrHiIiIiIiJSvPUheBj6WOAiYKC73xjvzvE20+pL8FyR/oABXYE6wATgRaB9/PUVERERESnBSlefkcvd/VHgufULzOzKcNkWxfsE9k7u/qy7L3P3pe7eDzjG3d8Gqm19nUVEREREpAQ4p5Bl3ePdOd5gJNfMTjWztHA6NWZd6Yr9REREREQ2x4tg2gIze9HM5prZ75tYb2b2mJlNNLPfzKxVzLpOZjYhXNdnE/ufbmYfA03M7KOYaTCwYMs1DMTbTOtM4FHgqXD+R6CbmZUDesZbmIiIiIiIFImXgSeAVzex/migaTjtBzwN7Gdm6cCTwJHAdGC4mX3k7n8U2P8HYBZQE3goZvky4Ld4KxnvaFqTgM6bWP1dvIWJiIiIiJR0qfCcEXcfZmaNN7PJ8cCr7u7AT2ZW1czqAo2BieHnf8zsrXDbfMGIu08FpgIHbE894x1Nq0E4ctZcM5tjZu+ZWYPtKVhERERERLaNmfUwsxExU4+tPER9YFrM/PRw2aaWb6oeJ5nZ32a2JBxxd5mZLY23EvE203qJYCSt/4Tz3cJlR8ZbkIiIiIhIqVAEmZFwQKl+23GIwh6G4ptZvin3A53d/c9tqUS8HdhruftL7p4dTi8DtbalQBERERERSbrpQMOY+QYEj/LY1PJNmbOtgQjEnxmZb2bdgDfD+dPZil7yIiIiIiKlRgr0GYnDR0DPsE/IfsASd59lZvOApmbWBJhB8HzBMzZznBFm9jbwAbBm/UJ3fz+eSsQbjJxH0Bv/YYLL+0O4TEREREREUoyZvUnwYPKaZjYduBXIBHD3Z4CBwDHARGAlcG64LtvMegJfAOnAi+4+bjNFVQ73PypmmQOJC0bc/V+gSzzbioiIiIiUZikymtbpW1jvwGWbWDeQIFiJp5xzt752G8QVjIRpmssJhvrK28fdFaCIiIiIiJRSZvYShTRMc/e4WlHF20zrA+AF4GMgN97KiYiIiIiUOl7YgFQl1icxr8sCJ7L5Du/5xBuMrHb3x7amViIiIiIipVIKNNMqKu7+Xux82Ffl63j3jzcYedTMbgW+JH8v+VHxFiQiIiIiIiVeU6BRvBvHG4zsBZwFHMaGZloezouIiIiISCgVOrAXFTNbxoaHJTowG7gu3v3jDUZOBHZy97VbXUMRERERESmR3L3S9uwfbzDyK1AVmLs9hYmIiIiIlHilKDMCYGZdgEPD2SHu/snmto8VbzCyAzDezIaTv8+IhvYVERERESmlzOxeoA3wRrjoSjM7yN2vj2f/eIORW7elciIiIiIipU1p6jNC8BT3lu6eC2BmrwCjgcQFI+4+1Mx2BJq6+9dmVp7g8fAiIiIiIlK6VQUWhq+rbM2O8T6B/UKgB1Ad2BmoDzwDHL41hYmIiIiIlHilKzNyDzDazAYTjKh1KHFmRSD+ZlqXAW2BnwHc/W8zq72VFRURERERkRLE3d80syEE/UYMuM7dZ8e7f1qc262JHdbXzDIobTGfiIiIiEg8vAimFGFmJwIr3f0jd/8QWG1mJ8S7f7zByFAzuwEoZ2ZHAu8CH291bUVEREREpCS51d2XrJ9x98VsxeBX8QYjfYB5wFjgImAgcFP8dRQRERERKR3Mo59SSGHxRLxdQeIeTSvXzD4APnD3efEeXERERERESrQRZtYXeJKgAdnlwMh4d95sZsQCt5nZfGA8MMHM5pnZLdtTYxERERERKREuB9YCbxN05VhNMPhVXLaUGbkKOAho4+6TAcxsJ+BpM+vl7g9vS41FRERERKT4c/cVBF06tsmWgpGzgSPdfX5MgZPMrBvwJaBgREREREQkVmr16YiUmTUD/gs0Jia2cPfD4tl/S8FIZmwgEnPweWaWuRX1FBERERGRkuddgoehPw/kbO3OWwpG1m7jOhERERGRUinFRruKWra7P72tO28pGNnbzJYWstyAsttaqIiIiIiIlAgfm9mlwABgzfqF7r4wnp03G4y4e/r21U1EREREpJQpXZmRc8Kf18Qsc2CneHaO+4EkIiIiIiIisdy9yfbsH+8T2EVEREREJB5eBFOSmdm1Ma//U2Dd/8V7HAUjIiIiIiKytbrGvL6+wLpO8R5EzbRERERERBKolIymZZt4Xdj8JikYERERERFJpNIRjPgmXhc2v0kKRkREREREZGutfwSIAeViHgeyVY8AUTAiIiIiIpJApaGZVqIeAaIO7CIiIiIikhTKjIiIiIiIJFIpyIwkijIjIiIiIiKSFMqMiIiIiIgkkjIjcVNmREREREREkkKZERERERGRBCoNo2klijIjIiIiIiKSFMqMiIiIiIgkkjIjcVNmREREREREkkKZERERERGRRFJmJG7KjIiIiIiISFIoMyIiIiIikkAaTSt+yoyIiIiIiEhSKDMiIiIiIpJIyozETcFIirij5fEcukMzFq5ZwUlDngKg566H0aHuruS6s3DNCm4a/QHz1izjgFo7cdXuR5KZls663Bwe+uNLfpk/GYDLdzucLg33pnJmWfYb+H/5yuhYb08u2bU97vDX0tlcN+o92tRozLXNO+Vt06RiTa4d+T++mT0+b9n1zY/hhEYtNzqelDz/d18ZfvgpnWpVnddeWgXA3xPTePDhMqxaBXXqOLfeuJoKFWDdOnigbxnGT0jDDK68fC2tWuYA0PvasixYYOTkwN4tcul95RrS04MyBg3O4KVXsgBnl51zue3mNQA89WwWP/4UbNT9rHUcflh2vro9/FgWAz/L5KvPVhTNxZCkmTUX+twN8xeCpcGpneHsU2DxUuh9G8yYDfXrwMO3Q5VKwT4T/oFbH4TlKyHN4N1noUwZeOQ5+PALWLocRn6+oYx7noBfRgevV62GhYvhl0/hz7/h9r7BcdLT4KKz4JjDgu1uvA/GTQB3aNwQ/q8PVChfhBdGityAR1bx1y/ZVKhq9HyqIgDv3LuS+dNzAVi9wilbwbj0iYrkZDsfPraamRNzyM2BlodncuipZQD4bcg6hr2zBjOoVN04+b/lqFBlQ+OUcd+t4+17VnHRIxWo3zR4H/zyxdX8NSJ4H2zXtQx7HZoJwKLZubxz30pWLYd6O6dx0tXlyMi0IrsmIommYCRFfPjvGN6c/At373Ni3rKX/vmeJyZ8A8AZTfbj4l3bcedvn7BozUp6/tyfeWuWsUul2jyz/1kc8dVDAAydM4E3J//Mp4dfke/4jSpU5/ymh3D2dy+wdN1qqmdVAGD4gin8Z+gzAFTOLMfAw6/gh3n/5O23R5V6VMosG+m5S+o4ptM6Tj5xHXfdUyZv2X0PluGyi9ewT8tcPhmYQf+3s7jwvLV89Enwj/HVF1exaJFx9XVlef6ZVaSlwZ23BgGLO9x0a1kGD83giMOymTbdeL1/Jk89vpLKlWDRouAf6A8/pvPX32m89Pwq1q2FnleVY//9sqkQ3KaMn5DG8uX6Z1tapKfDtZfBns1gxUo4+UI4sDUM+AwO2BcuPBOeeyOY/nsxZGfDtXfBfTfCbrvAoiWQEf53a38gnHESHH1m/jKu77nh9evvBUEIQNmycO+N0LgBzJ0flH1wG6hcKdinYnhP3vsE9B8Q1EVKrn2OyGS/47J4v++qvGWn9tkQgX7+/GrKlA/em8Z9l032OqfnUxVZu9p54pLl7NUuk8o1jc/6rabn0xWoUCWNL15czc+frOWwM4P/rWtWOj99tJYGu6bnHXfCL+uY+U8OlzxegZx18OJ1K2jaOoOy5Y0vX1rNgSeUYa92mXz0xCpGfbmOtsdmFdEVkXipz0j8IuszYmb3m1llM8s0s0FmNt/MukVVXnE3cuFUlqxdlW/Ziuw1ea/LpWflZfzGL53NvDXLAJi4bC5l0jPITAvexH5bNJ35a5ZvdPyTd9yXtyb/wtJ1qwFYuHbjb5ePqrcH382dyOqcdQCkYVy951H0/ePL7T4/KR5a7p1L5cr530H/nZZGy72DbwHbtM5h6LDgU96Uqca+rYJMSLVqTqWKzvgJwVvK+iAiJwfWZcP6MOLjTzI56YR1VA6/za5WzcNjpdFy7xwy0qFcOdhl51x++iUj7xhPPpPFJRetjeq0JcXUrhEEIhBkHnbeEebMg2++h+PDRO7xnWDQd8Hr70fArjsHgQhAtSrkZeJa7hkcb3M+HQTHHB68btIwCEQAateEGtVg4ZJgfn0g4g6r17DhxpYSq3HzDMpVKvwX7e78/u06WrTb8L3u2tWQk+Nkr3XSMywIVDy4Z9atCfZZs9KpXH3Dx69Br6/h4FOyyIiJJ+ZNy6XxXhmkpxtZZY06TdKZODIbd2fybznscXBQZsvDM/nzp3XRnLxIEYmyA/tR7r4UOA6YDjQDromwvBLp8t0O56sje3Nsg714cvw3G60/su4ejF8yi3W5OZs9TuMKNdixYg1ePfh8Xj/4Ag6qtctG23Sq15yBM8bmzZ/eZD+GzJ5QaHAjpcdOTXL57vvgk93gIRnMmRv8Y95l51y+/T6D7ByYOcuY8Fc6c+du+Kfd+5qyHHdiBcqXc9q3C5oaTJuexrRpaVzSsxw9Li3HT7+k5x3r558zWL0aFi+BUWPSmTsvONZ7AzI5+MAcatbQ10yl0YxZQdZi7z1gwaINgUXtGrBwUfB6yrTg5wX/hZMugOf7b8XxZ8P0WbB/q43X/fZn0ByxUb0Ny264Bw45ESb/C91O2rZzkpJh6rgcKlY1atQP3sf2PDiDrLLwQLflPNR9OQedlEX5SkZ6htH5srI8eelyHjhrOfP+zaXVUUFmedY/OSydl8uubTPzHbtOk3T+HpHN2tXOiiW5TP4tmyXzclm51ClbAdLTg/fHKjXTWLZA740pyYtgKiGiDEbW/2UdA7zp7gu3tIOZ9TCzEWY2YuEXIyOsWvHx+PhBHPlVXz6dPpbTm+yXb93OlWrRa48juf3Xj7d4nHRLY8cKNTjv+5e4btT/uL1lFyplbGh+VbNMRZpW3oEf5k4EoFaZShxVbw/6T/45sSckxc71167m/Q8zOa9HOVaugszwL/vYY7KpXSuXCy4qx2NPlKF585y8b6MB+j6wmg/fW8G6dcao0cGKnByYNiONxx9ZxW03r+a+B8qwbDm0bZPD/vtnc3HPctx2Z1ma75FDehrMn28MHprBySfpm7/SaMVKuOIW6HP5hqxEYXJyYNRYeOAmeOMJ+Ppb+DHOfyEDv4GO7ch37wLMXQDX3Q1394G0mP+U/3c9DH0PdtoRPtv4+yEpRcYOXcde7TYEEdP/yiEtDa55rSK9XqzI9wPWsnBWLjnZzi8D13LJ4xW55rWK7NAkjWHvriU31/nsudV0vGDjptC7tMqgWesMnv/vCt69fxUNd08nLX2jzURKhCiDkY/NbDzQGhhkZrWA1Zvbwd37uXtrd29dveO+EVat+Bk44zeOqLt73vwOZSvzSJuu3DD6faavXLTF/eesXsrg2ePJ9lxmrFzM5OULaFSxet76jvWa882sP8n2oDnOblXq0KhCdT49/Ao+P+IqyqZnbtQPRUqHHRs5Dz+wmhf7reKIw7KpXy+4RzLS4YrL1vLy86u49+7VLF9uNGiQm2/fMllw8IHZfBtmVmrVcg45KJuMDKhX12nUMJfp04O3oXO6rePl51fxyIOrcYeGDXL56+80Zswwup5ZnlO6lmf1GjjtTPUYLg3WZcOVt0DnI+CoQ4NlNaoFQQIEP6tXC17vUAvatIRqVaFcWTh0f/jjr/jK+WwQHHtE/mXLV8DF18GV5wfNvApKT4ejD4Mvh23LmUlJkJPj/PFDNs0P3RCMjB2yjl32zSA9w6hYNY1Ge6Qzc2IOsycF74vV66ZhZjQ/JJNpf+awdhXMnZrLS31W0PfcZUwfn0P/O1Yy4++gpUO7rmW49ImKdL+7Au5Qo14a5Ssbq1cE5QMsmZ9LpRpqL5iSlBmJW5TByK3AAUBrd18HrAS6RFheidOowoZgoUOd3Zi8fD4AlTLK8uR+Z/Lon18zZuG0uI71zazxtKnZBICqWeVpXLEG01dsCGKOrp+/ida3c/+mw5cP0unrR+j09SOszlnHsYMeS8RpSTGzvpN5bi688loWx3cOshSrV8OqsJvT8BHppKdDk8bOylUwf0GwT3YO/PhzOjs2Ct41Dzk4Oy9LsnhJ0GyrXt1ccnJgSdguf+I/afwzKY02bXI48IAcPnp/Jf97K5jKloG331hZhGcvyeAON90XZB+6n7Zh+WEHwYfhiFgffh7MAxzcNhhNa9XqoDP78F9h58ZbLmfyv7Bkef6AY+06uPwmOL4jdOqQv05Tp294PeQH2KnRdp2mFGOTRudQs0EaVWpu+BhVpVYak3/Nwd1Zu9qZPj7YplINY96/uaxYEgQl/4zOplbDNMpWMPq8WYneLwVTg93SOeOW8tRvmk5ujrNyabD97Mk5zJmSy86tMjAzmuyVzh/fBU1fxwxax+77ZW5cQZFiJMrRtH5097xWuO6+wsy+BQppmSv3tTqFNjUbUzWrPF8f2ZsnJwzhkNpNaVyxBo4zc+US7vwtaI51epO2NKxQnYuateOiZu0AuOjH11i4dgW99jiSY+vvRdn0TL4+sjfv/TuKpycM4ft5Ezmw9s580OEyct15aNyXLFkXfJKsV64qdcpVYcSCqUk7f0kNt95ZhjFj0lm8xDjxP+U5v/taVq4y3v8w+GfX7pBsjj06+Ce4aLHR+9pypBnUrJnLzdcHic/Vq4w+N5Zl3bqg+cy+rXI4vksQwOzXJofhw9Pp1r08aWnOpRevpUoVWLMWLrsyyHiUL+/ccuMaMtQkodQaNRY++tJotpNz4vnBsqsuhAvOCIb2/d+nUG+HYGhfCIb37X4q/OciMIND94P2BwTrHng66KC+ajW0PwVOORZ6nhus+3RQMGyvxXyx/PlgGPFrMIzwB2Hg8399gg7y198TZE0c2G1nuLV3EVwMSap371vJ5LE5rFzqPHj2MjqcWYZ9O2Yxdtg6WrTLHwS0PS6LDx5exROXBjfJPkdmUqdJ8EbW4YwyvHDtStIzoErtNE7qtflRKnNy4IVrgy9eypQ3Tr66XF4/kSPPLcu7969k0GurqbtTOq06KhhJRamQrzKzTsCjQDrwvLvfW2D9NcD6MQEzgN2BWu6+0MymAMuAHCDb3VtHVk/3xOZ5zKwOUB94HTiDDb+PysAz7r5bPMfZ66NbS1ACSoqrb1o/n+wqiFAjbTMdJkSK0LvLqyS7CiKctsvwVPisv1ktej0c+efY3x7utcnrYGbpwF/AkQQDSQ0HTnf3PzaxfWegl7sfFs5PIWjdND/R9S4oisxIR6A70ADoG7N8GXBDBOWJiIiIiMgGbYGJ7j4JwMzeAo4HCg1GgNOBN4uobvkkPBhx91eAV8zsZHd/L9HHFxERERFJZUXx0EMz6wH0iFnUz937ha/rA7Edi6cD+Ydl3XCc8kAnIOZxsDjwpZk58GzMcRMu4cGImfUu7PV67t634DIREREREYlfGCBsKkgorAnXpkKkzsD3BR7DcZC7zzSz2sBXZjbe3SMZQzCKZlqVIjimiIiIiEjxkPyez9OBhjHzDYCZm9i2KwWaaLn7zPDnXDMbQNDsq3gEI+5+e6KPKSIiIiIicRsONDWzJsAMgoDjjIIbmVkVoB3QLWZZBSDN3ZeFr48C7oiqopEN7WtmL1FIXOju50VVpoiIiIhI0iU5M+Lu2WbWE/iCYGjfF919nJldHK5/Jtz0ROBLd18Rs/sOwAALxj3PAPq7++dR1TXK54x8EvO6LMHJbio9JCIiIiIiCeLuA4GBBZY9U2D+ZeDlAssmAXtHXL08kQUjBUfSMrM3ga+jKk9EREREJBUUxWhaJUVaEZbVFGhUhOWJiIiIiEgKi7LPyDKCFnMW/pwNXBdVeSIiIiIiKUGZkbhF2UxLQ/yKiIiIiMgmRfHQw1abW+/uoxJdpoiIiIhIqlCfkfhFkRl5KPxZFmgN/ErQVKsF8DNwcARlioiIiIhIMZPwDuzu3sHdOwBTgVbu3trd9wX2ASYmujwRERERkZTiRTCVEFGOprWbu49dP+PuvwMtIyxPRERERESKkSgfevinmT0PvE4Qv3UD/oywPBERERGRpFOfkfhFGYycC1wCXBnODwOeirA8EREREREpRiJrpuXuq939YXc/0d1PBIYDfaMqT0REREQkJajPSNyizIxgZi2B04HTgMnA+1GWJyIiIiIixUcUzxlpBnQlCEIWAG8DFo6wJSIiIiJSspWgzEXUosiMjAe+BTq7+0QAM+sVQTkiIiIiIlKMRdFn5GRgNjDYzJ4zs8MJHnooIiIiIlLimUc/lRRRPPRwgLufBuwGDAF6ATuY2dNmdlSiyxMRERERkeIpytG0Vrj7G+5+HNAAGAP0iao8EREREZGUoNG04hbpaFrruftC4NlwEhEREREpscxLULQQscgyIyIiIiIiIptTJJkREREREZFSQ4mRuEWaGTGzHc3siPB1OTOrFGV5IiIiIiJSfEQWjJjZhcD/2NBPpAHwQVTliYiIiIikAg3tG78oMyOXAQcBSwHc/W+gdoTliYiIiIhIMRJln5E17r7WLHjeoZlloBZ0IiIiIlLS6RNv3KLMjAw1sxuAcmZ2JPAu8HGE5YmIiIiISDESZTDSB5gHjAUuAgYCN0VYnoiIiIhI0qnPSPwia6bl7rnAc+EkIiIiIiKST8KDETMby2Zayrl7i0SXKSIiIiKSMkpQ5iJqUWRGjovgmCIiIiIiUsIkPBhx96mJPqaIiIiISHFRkvp0RC2yPiNmtoyNk1RLgBHA1e4+KaqyRUREREQk9UX5nJG+wEygP2BAV6AOMAF4EWgfYdkiIiIiIsmhzEjcohzat5O7P+vuy9x9qbv3A45x97eBahGWKyIiIiIixUCUwUiumZ1qZmnhdGrMOsWLIiIiIlIi6Tkj8YsyGDkTOAuYC8wJX3czs3JAzwjLFRERERGRYiDKhx5OAjpvYvV3UZUrIiIiIpJUXoJSFxGLcjStWsCFQOPYctz9vKjKFBERERGR4iPK0bQ+BL4FvgZyIixHRERERCRllKQ+HVGLMhgp7+7XRXh8EREREREpxqLswP6JmR0T4fFFRERERFKPF8FUQkQZjFxJEJCsMrOlZrbMzJZGWJ6IiIiIiBQjUY6mVSmqY4uIiIiIpCrLTXYNio+EByNmtpu7jzezVoWtd/dRiS5TRERERCRllKBmVFGLIjPSG+gBPFTIOgcOi6BMEREREREpZhIejLh7j/Bnh0QfW0REREQk1Wlo3/glvAO7mbUxszox82eb2Ydm9piZVU90eSIiIiIiUjxFMZrWs8BaADM7FLgXeBVYAvSLoDwRERERkdThHv1UQkTRZyTd3ReGr08D+rn7e8B7ZjYmgvJERERERKQYiiQYMbMMd88GDifozB5leSIiIiIiKUN9RuIXRXDwJjDUzOYDq4BvAcxsF4KmWnFpcOmiCKomsnXO5uRkV0EEcnKSXQORQLbuRUm+0+YluwaSSFGMpnW3mQ0C6gJfuuc1aksDLk90eSIiIiIiKUWZkbhF0YEdd//J3Qe4+4qYZX/pgYciIiIiItEzs05mNsHMJppZn0LWtzezJWY2JpxuiXffRFIfDhERERGRBEp2nxEzSweeBI4EpgPDzewjd/+jwKbfuvtx27hvQkSSGRERERERkaRpC0x090nuvhZ4Czi+CPbdagpGREREREQSqQieM2JmPcxsRMwUO4JtfWBazPz0cFlBB5jZr2b2mZntuZX7JoSaaYmIiIiIFDPu3o9NP1DcCtulwPwoYEd3X25mxwAfAE3j3DdhlBkREREREUkg8+inLZgONIyZbwDMjN3A3Ze6+/Lw9UAg08xqxrNvIikYEREREREpWYYDTc2siZllAV2Bj2I3MLM6Zmbh67YEccGCePZNJDXTEhERERFJpCSPpuXu2WbWE/gCSAdedPdxZnZxuP4Z4BTgEjPLJnhQedfw+YCF7htVXRWMiIiIiIiUMGHTq4EFlj0T8/oJ4Il4942KghERERERkQRK9nNGihP1GRERERERkaRQZkREREREJJFylRqJlzIjIiIiIiKSFMqMiIiIiIgkkhIjcVNmREREREREkkKZERERERGRBNJoWvFTMCIiIiIikkiuaCReaqYlIiIiIiJJocyIiIiIiEgCqZlW/JQZERERERGRpFBmREREREQkkZQZiZsyIyIiIiIikhTKjIiIiIiIJJBpNK24KTMiIiIiIiJJocyIiIiIiEgi5Sa7AsWHMiMiIiIiIpIUyoyIiIiIiCSQ+ozET5kRERERERFJCmVGREREREQSSYmRuCkzIiIiIiIiSaHMiIiIiIhIIqnPSNyUGRERERERkaRQZkREREREJIFMiZG4KTMiIiIiIiJJocyIiIiIiEgiqc9I3JQZERERERGRpFBmREREREQkgSw32TUoPpQZERERERGRpFBmREREREQkkdRnJG7KjIiIiIiISFIoMyIiIiIikkhKjMRNwYiIiIiISAKZmmnFTc20REREREQkKZQZERERERFJJGVG4qbMiIiIiIiIJIUyIyIiIiIiiaSHHsZNmREREREREUkKZUZERERERBJIo2nFT5kRERERERFJCmVGREREREQSSZmRuCkzIiIiIiIiSaHMiIiIiIhIIikzEjdlRkREREREJCmUGRERERERSSQ9ZyRuyoyIiIiIiEhSKDMiIiIiIpJAes5I/BSMpKBeD55B2yP2ZPH8ZVxyxL351p180WFccPMJnLbX9SxdtIIOJ7bm5IsPy1vfZPd6XN7pASb9MYNDO+9D1yuOIi0tjV++GceLd38EQI9bT6TFgU0BKFMui6o1KvKfPfsA8MnUR5gyfiYA82Ys4vbzniuKU5YUVdi9eGbvo+l0xgEsWbAcgFfu+4Th3/zBPofsyrnXdyEjK53stTm8cNcH/PrD3wC0O74Vp11+FLizYM5SHrj8VZYuWkGtetW4+pFuVKxcjrR046V7Pmb4N38AcMQpbel65VEAvPXol3z9v1+ScAUkFfTq2422RzYP7sMOdwNw1rXHcUDHFuTmOksWLOOhK19j4ZwldDipDSdfckTevk32qMflR93HpHHTObRLK7pe2Ym09DR++fp3XrzrAwBqN6hOr77dqFKjIssWr+CBnq8wf9ZidtqzAT3vPY3ylcqRm5PLW49+zrCPRiXjEkgK6PXoWbQ9cq/gPjz0TgAO7tKKbtccR8NmdbjqqHv5+9d/87Y/9cqOdDzzIHJzcnn6hncYNTh4b8vITOfSe7uy10HN8Fznlf/7kO8/GU2PO/9Di4ObAeH/5pqV+M8uvdmpeQN63n8G5SuVDe7DRz5j2Acji/4CiEREwUgK+urdn/no5WH895Fu+ZbXrFuVfQ7ZlTnTF+YtGzxgBIMHjACg8W51ueWFC5n0xwwqVS3P+TcdzxVHP8iShcu5+uEzaXlQM8Z8/xf9bh+Qt3+Xcw9l5z0b5M2vXb2Onh3vj/gMpbjY1L34wXNDeO/Zb/ItW7pwBbed+ywL5yxlx13rctcbl3BW61tIS0/j4ttP5qIO/8fSRSs478YudD73UN7o+xmnX3kU3348mk9f+45GTetwx6sX0f2A26lYtTxn9OrEFcc+CO48NvAafvpqLMuXrCrK05cU8dU7P/HRS0P572Nn5y1776mvee3+TwDocn57zuh9NE9c9xaD3x/O4PeHA9B4t3rc8vJFTBo3nUrVKnD+LSdyRcf7WLJgOVc/ehYtD96VMd9N4IJbTmTQuz/z9bs/s/dBzeh+w/E8ePkrrFm1lgeveJWZk+dRfYcqPP7FdYwc8icrluo+LI2+eutHPnphCP99onvesql/zuTO7s9yxUNn5tu2UbO6tDuhDRcffAfV61Thnv9dxQX730JurtO119Esnr+MC/e/FTOjUrXyAPS7+d28/btc0J6d92oIwJqVa3mw58vMnDQ3uA8H3cDIb/7QfZjqlBmJW2R9RszsIDOrEL7uZmZ9zWzHqMorSX7/+R+WLV650fKLbjuJF+7+cJM3eLvj92Xoh8G3JXV3rMmMSfNYsjD49nr0d39x0DF7F7rPkA/1DYsUblP3YmH+GTedhXOWAjB1wiyyymSSmZWBGZgZZctnAVC+YlkWzlkCBLdy+Uplg+WVyrIg3H/fdrsx+tsJLF+8kuVLVjH62wns2373RJ+eFBO//zSRZYtW5Fu2cvnqvNdly2dBIW+L7U5szdAPgi9r6jaqwYx/5uZl9EZ/O4GDjm0JBB8cx3w3AYBfv/+LAzruBcCMSXOZOXkeAAvnLGHx/GVUqVExoecmxcfvP05k2aL874fT/p7NjH/mbLTt/ke3YOgHw1m3Nps5/y5g5pS5NGvVGICjzjiQtx/9HAB3Z+nCFRvt3+7ENgx5P7h3Z0yay8xJc4HwPpy3jCo1KyXy1ESSKsoO7E8DK81sb+BaYCrwaoTllWj7Hdmc+bMXM/nPmZvcpl3nVgz5MGhCMHPKPBrusgO1G1QnLT2NAzruRa161fJtX7t+Neo0rM6v3/+VtyyrTAaPfvpfHv6od94/ZJGCOnc/hKe+uo5eD55BxSrlNlp/8LEt+ef36axbm01Odi5P3PAOT399PW+MvJNGTevwxZs/AvB638/ocFJrXht+B3e8ejFP3/w/AGrWqcq8mYvyjjd/1mJq1qlaJOcmxcc5fTrz6oi76HBSG1574JON1rfr0oohYeZ4o/fETi3y3hMnjZueF5gceMzelK9UjkrVKuQ7VrOWO5KRlcGsKfOjPSkpEWrUrca8GTHvYTMXU7NuNSpUDt4vz+7ThccH3cANL1xI1Vr5A4vaDapTZ8ea/Prt+I2O22yfxmRkpTMrDJIlhblHP22BmXUyswlmNtHM+hSy/kwz+y2cfgg/s69fN8XMxprZGDMbkeCrk0+UwUi2uztwPPCouz8KbDaUN7MeZjbCzEZMW/F7hFUrXsqUzaTrFUfx2oMDN7nNrvvsyOrVa5k6YRYAy5es4onr3+H6p7vz4PtXMmfaQnJycvLt0+74fflu4Bhyczfc0GfvdytXHvsg9/V8hYtuO4m6O9aM5qSk2Pr01e8476A7uOyo+1k4dwkX3nxivvWNmtXhvOu78HiftwFIz0jj2LMOomen+zlz35uZPH4mp/Y8EoD2x+/L1+/8zFltbuGWs5/hmkfPwszANi7XlfKWAl6592PObn0Tg98fTudz2+Vbt+s+jVm9qsB7Yp+3uP7Z83nwg1753hOfv2MAex3QlCe+7MNeBzRl/sxF5GRveL+sVrsy1zx+Dg9f9ZruQ4mLbeI9LD0jjVr1q/PHL/9w+eH/x5/DJ3HBbSfn267dia357uNR+f43A1TboTLXPNWdh694VfehbJGZpQNPAkcDewCnm9keBTabDLRz9xbAnUC/Aus7uHtLd28dZV2jDEaWmdn1QDfg0/CiZG5uB3fv5+6t3b11wwrNI6xa8VK3cU3qNKzBU19ex8s/3krNulV5/PNrqBbzbUq7Lq0YWqBD289f/06vzn3pffzDzJg0lxkFvklp16UVQz7I3xlzfTOb2f8u4LcfJ7Jz8waIxFo8fxm5uY6781n/H2nWslHeupp1q3Lz8xfw4FWvMWtq8A3y+j5J6+e//Xg0e7RuAkDHrvsz7OPRAIwfNYXMMhlUrl6B+bMW58vk1axblQVh0y6RgoYMGJGX2Viv3Qn7bvye+NXv9Dr2AXp3fogZ/8xhxqQNTbDuOv85eh51L6/c8zEAK5cFzcDKVyzLHa9fwiv3fcz4UVMiPxcpGebPXESt+jHvYfWqsmD2YpYuXMHqFWv44dMxAHz70Sh2adEo377tTmzNkLDf03rlK5bljv49eeWejxg/cnLk9ZcESH5mpC0w0d0nufta4C2CBEFMFf0Hd1+fwvsJSMqHviiDkdOANcD57j4bqA88EGF5JdaU8bM4veWNdD/gdrofcDvzZy3m8k4PsGjeMiBoj3/IcfswtMAoL+vbNlesUo5jzz6YL/r/mLeu/k61qVilHH/GvKlVrFKOzKxgTIPK1SqwR5sm/PvX7KhPT4qZarUr570+sFOLvG+eK1Qux+2vXMTL937MHyM23FfzZy+mUdM6VKke3I/7HLIr//4dtLGeO3MRLcPRYxrusgNZZTJZsmA5I4eOp9Whu1GxSjkqVilHq0N3Y+TQjZssSOlVr0mtvNf7H7UX0yduaLef9574Qf6WBfneE885lC/6/wBA5eoVgowccNoVR/HlW8F7ZUZmOje/2INB7/7Cd5+MjvR8pGT56fPfaHdCGzKzMtihUQ3qNanNX2Ew+/OXv9HioOB9r+Whu/HvX7Py9qu/8w5UrFKBP4dPyluWkZnOza9czKB3fuI7jeYm8asPTIuZnx4u25Tzgc9i5h340sxGmlmPCOqXJ5LRtMIsyOvunje+orv/i/qMxOW6J86hxQG7ULl6RV4bfgevPTSQL9/6aZPbN99/Z+bPWszsfxfkW37x7Sez0x7Bfdf/kc/zZUban7DvRsFLw13qcPl9p+G5jqUZ7zz5Nf/+rWCkNCvsXmxxQFN22rM+uDNn2kIeC5tjde5+CPUa1+T0Kzty+pUdAbjxjKdYOGcpbzz8Ofe/dwU52TnMnb6Ih3q9DsDzd3zAFfd35cQLO+Du9O39BgDLF6/kzUe/4NFP/wsE9+/yODvSS8lz3VPn0uLApsF9OPIuXnvwU9ocvicNdt4Bz3XmTl/I49e9mbd98/13Kfw98c7/BPcu0L/vZ8wIOwW3OKAZ3W/ogrvz+08TeeqGdwA4pEsrmu+/C5WqVeCIU/cHoO9VrzFp3PSiOG1JMdc9ez4tDmoW3Ie/3sNr93/M8kUrueSe06hSoyK39+/JpHHTuOnUx/l3wiy+/Wgkz353Kzk5OTzV5628Zlcv3jGA/z51Lhfd9R+WLFhO3yteySuj/UltGPpB/qzIIcfvS/MDmlKpegWO6HoAAH0vf4VJv+s+TGlF8AT2MEiIDRT6ufv6plaFNBYsbKgPMLMOBMHIwTGLD3L3mWZWG/jKzMa7+7BE1Huj8qNqd2hmHwFnufs2ta04usEVahApIgJQoL+XSNJk616U5Pts3jOFfdBOKZ32vDHyz7Gfj7t7k9fBzA4AbnP3juH89QDufk+B7VoAA4Cj3f2vjQ4UbHMbsNzdH0xQ1fOJ8jkjq4GxZvYVkDdunbtfEWGZIiIiIiJJlQJPYB8ONDWzJsAMoCtwRuwGZtYIeJ8gefBXzPIKQJq7LwtfHwXcEVVFowxGPg0nEREREZHSI8nBiLtnm1lP4AsgHXjR3ceZ2cXh+meAW4AawFNhv7nscOSsHYAB4bIMoL+7fx5VXSMLRtz9FTPLApqFiya4+7qoyhMRERERkYC7DwQGFlj2TMzrC4ALCtlvErDxk7IjElkwYmbtgVeAKQSdaBqa2TlRdX4REREREUkJuUlvplVsRNlM6yHgKHefAGBmzYA3gX0jLFNERERERIqJKIORzPWBCIC7/2Vmm33ooYiIiIhIsZf8DuzFRpTByAgzewF4LZw/Exi5me1FRERERKQUiTIYuQS4DLiCoM/IMOCpCMsTEREREUk+ZUbiFuVoWmuAvuEkIiIiIiKST5SjaR0E3AbsGFuOu+8UVZkiIiIiIkmnzEjcomym9QLQi6CfSE6E5YiIiIiISDEUZTCyxN0/i/D4IiIiIiKpR88ZiVuUwchgM3sAeB9Ys36hu4+KsEwRERERESkmogxG9gt/to5Z5sBhEZYpIiIiIpJcnpvsGhQbUY6m1SGqY4uIiIiISPGX8GDEzLq5++tm1ruw9e6uoX5FREREpOTSaFpxiyIzUiH8WSmCY4uIiIiISAmR8GDE3Z8Nf96e6GOLiIiIiKQ8jaYVtyiaaT22ufXufkWiyxQRERERkeInimZaFwO/A+8AMwGLoAwRERERkdSkPiNxiyIYqQv8BzgNyAbeBt5z90URlCUiIiIiIsVUWqIP6O4L3P2ZcGjf7kBVYJyZnZXoskREREREUo579FMJEdlzRsysFXA6cCTwGTAyqrJERERERKT4iaID++3AccCfwFvA9e6enehyRERERERSUgnKXEQtiszIzcAkYO9w+j8zg6Aju7t7iwjKFBERERGRYiaKYKRJBMcUERERESkecnOTXYNiI4qHHk5N9DFFRERERIoNNdOKW8JH0xIREREREYlHZKNpiYiIiIiUSsqMxC3SzIiZlTOzXaMsQ0REREREiqfIghEz6wyMAT4P51ua2UdRlSciIiIikhJyPfqphIgyM3Ib0BZYDODuY4DGEZYnIiIiIiLFSJR9RrLdfUn4jBERERERkVLBXUP7xivKYOR3MzsDSDezpsAVwA8RliciIiIiIsVIlM20Lgf2BNYAbwJLgasiLE9EREREJPnUZyRukWVG3H0lcGM4iYiIiIiI5JPwYMTMPgY2Ga65e5dElykiIiIikjL0nJG4RZEZeTCCY4qIiIiISAmT8GDE3Ycm+pgiIiIiIsVGrkbTildkfUbMbCwbN9daAowA7nL3BVGVLSIiIiIiqS/KoX0/A3KA/uF8V8AIApKXgc4Rli0iIiIikhzqMxK3KIORg9z9oJj5sWb2vbsfZGbdIixXRERERESKgSiDkYpmtp+7/wxgZm2BiuG67AjLFRERERFJGlefkbhFGYxcALxoZhUJmmctBS4wswrAPRGWKyIiIiIixUCUDz0cDuxlZlUAc/fFMavfiapcEREREZGkUp+RuEU5mlYZ4GSgMZBhZgC4+x1RlSkiIiIiIsVHlM20PiQYOWsksCbCckREREREUkeuMiPxijIYaeDunSI8voiIiIiIFGNRBiM/mNle7j42wjJERERERFKLazSteEUZjBwMdDezyQTNtAxwd28RYZkiIiIiIlJMRBmMHB3hsUVEREREUpKrz0jcEh6MmFlld18KLEv0sUVEREREUp6aacUtisxIf+A4glG0nKB51noO7BRBmSIiIiIiUswkPBhx9+PCn00SfWwRERERkVSnZlrxS0v0Ac1sx/Cp6+vnO5jZo2bWy8yyEl2eiIiIiIgUTwkPRoB3gAoAZtYSeBf4F2gJPBVBeSIiIiIiqcNzo59KiCj6jJRz95nh627Ai+7+kJmlAWMiKE9ERERERIohc09smzYzG+vue4WvRwHXu/sX4fxves5I0TGzHu7eL9n1ENG9KKlA96GkAt2HIvlF0UzrGzN7x8weBaoB3wCYWV1gbQTlyab1SHYFREK6FyUV6D6UVKD7UCRGFM20rgJOA+oCB7v7unB5HeDGCMoTEREREZFiKIqhfR14q5DloxNdloiIiIiIFF9RNNOS1KE2qZIqdC9KKtB9KKlA96FIjIR3YBcREREREYlHFA897GdmJ5pZpUQfW0RERERESo4ohvbdH+gEHE4wetaXwOfu/mtCCxIRERERkWIt0mZaZlYDOAo4GtgLGE0QmLwTWaEikvLMzFxtRCUF6F6UVGBm6e6ek+x6iCRDkfYZMbN9gU7ufneRFSr56A1PksnM6gHLgdXurucOSdKYWRNgGZDt7ouTXB0ppcysNTDT3WeaWZq75ya7TiJFTR3YSwEz6wIc5u5XhfMKSKTImdlxwH+BbOAr4B13n5zcWklpZGbHAjcD04HfgSeABcqQSFEys8bAj8BU4BR3n66AREqjKB56KCnEzNoCTwIVzay2u5/h7jkKSKQomdnhwP3A6UAV4BxgD0DBiBQpMzsKuIvgKdhrgduBLAUiUtTcfYqZvQ9UAAaY2WnuPinZ9RIpanrOSMlXHbjC3asBu5vZmwDrA5LkVk1KkRbAk+7+q7sPA4YDXc0szcwsyXWT0mU34AZ3Hw7MBHYH7jez3mHQLBI5M0s3swwgF3geeBt42cxODlsziJQaUQzt283Mzipk+YVmdkaiy5PNc/fPCdLAAK2AZmb2drgux8x2SFrlpNRw94eB9yDoMAxMBMq6e667u4YCl6Li7o+5+2dmVpbgQ+CLwKPAOuBkM6uiAFmi5u457p4NfAs0d/cHCTLF/YEaAGamL4ylVIiimdbVwKGFLH8LGELwhyYRMrP2QFOgXPiPd7aZZbn72rDZ1i9m9hzwBXComV3n7quSWGUpgWLuw7Lu/ri7zwYIg49phO8/ZtYNqGdmj6hTu0Sh4HsigLuvNrOL1t+XZraSYEj6XDXZkigUfE8MF68GGpnZfsCBwLtAbzP7xt2nJqWiIkUsiqg73d2XFVwYLsuMoDyJYWbHAE8RXOurzOwpgDAQyQy/jdkXOA14FnhOgYgkWoH7sNf6+zBGLrDGzC4G+gAfKRCRKGzqPTE0J+b1rkBl9H9KIlDIe+LT4aqBBPfeF8C17t4NeB01o5dSJIqbPdPMKhRcGDbDyIqgPAmZWSPgJuByd38K2AfYy8x2DcfSXxdu1x5YABzq7mOTVV8pmbZ0H4ZNYFYDRwDnEowiMz55NZaSanP3IgRZunC7XsCNBP3rFiarvlIybeI+bG5muwFGkA052t0HhLvcr5EGpTSJIhh5AfhfOGQdkDd83VvhOonOGuAudx9kZlnASoIPfdULNDsoBxzp7uOSUUkp8TZ7H4amEXwT2EOBiERok/fi+g3MrDxQDTjH3X9PTjWlhNvce+I6gmHOf1w/oIeaCUppk/BgJOyE9SEw1MwWmNkCYCjwibs/kOjyJPjWxcwygUXuPhCCZlnhm9wkgiYxmNn+4brP3H1i0iosJdJW3IcHhLt0c/dfk1NbKcm24l5s6+4r3f0WBSKSaHHch+uH128bDrev/kpSKkXSJtHdn3H3HYEdgcbuvqO7P72l/WTrhQ/vGkjQFvW1MO1L+O0LBM90KG9mpwOvm1nd5NRUSrKtvA9fM7O6+qcrUdjKe7G/3hMlClv7vxmolZSKiqSAhI+mZWa9CyxyM5sPfKc2kIkTtrtvANwL9AT+BLoB35hZbBOsGcANBP11jnf3Wcmor5RMug8lVehelFSwHffh7GTUVyQVRDG0b2HPC2gM3Ghmt7n7WxGUWeqEw6POJHiGyN/AXHd/yMzWAV+a2WHuPgGYDZwCdFTbfEk03YeSKnQvSirQfSiy9ayoWkqYWXXga3dvVSQFlmBmtgtBh8tJBCngke5+f8z6a4E9gQuBvYHZYYdhkYTRfSipQveipALdhyLbJorMSKHcfWGYvpTtYGbHAf8HLALGAm8Aj4Wd3+4JN3sHuDF8bsPw5NRUSjLdh5IqdC9KKtB9KLLtiiwYMbPDCP5IZRuZ2YHAg8Dp7j7azPoBbQme2vqTmaUTDKF8MLCPmVXXmPmSaLoPJVXoXpRUoPtQZPskvJmWmY0FCh60OjATOFttI7dd+IbXzN1fDudrAS+7+7FmthPBQ5VWE7wJnut6oKFEQPehpArdi5IKdB+KbJ8ogpEdCyxyYIG7r0hoQaVQ+O1KBXdfGr6uC3wMHOPus8JrPyPcZkky6yoll+5DSRW6FyUV6D4U2T5RPPRwaoHpXwUiieHuOe6+NJw1YDGwMHyz60YwTGCm3uwkSroPJVXoXpRUoPtQZPsU2WhaEg0zexmYBRwFdFf6V5JB96GkCt2Lkgp0H4rET8FIMRWOTJZJ8EClTOBwd/87ubWS0kb3oaQK3YuSCnQfimw9BSPFnJl1B4bHPNVVpMjpPpRUoXtRUoHuQ5H4KRgp5szMXL9ESTLdh5IqdC9KKtB9KBI/BSMiIiIiIpIUCR9NS0REREREJB4KRkREREREJCkUjIiIiIiISFIoGBERERERkaRQMCIisp3MLMfMxsRMjc3shwQev72ZfVJgWW0zm2xmdWKWPWVmfRJVroiISNQykl0BEZESYJW7tyyw7MAoC3T3uWZ2H/Ag0M3MWgEHA/tu6zHNLMPdsxNVRxERkS1RZkREJAJmtjz8WdfMhoUZk9/N7JBweSczG2Vmv5rZoHBZWzP7wcxGhz933UIx/YCdzawD8ATQE2hkZp+b2Ugz+9bMdguP3dnMfg6P/bWZ7RAuv83M+pnZl8Cr0VwNERGRwikzIiKy/cqZ2Zjw9WR3PzFm3RnAF+5+t5mlA+XNrBbwHHCou082s+rhtuPDZdlmdgTwf8DJmyrU3XPN7BLgG+Ajdx8WBjYXu/vfZrYf8BRwGPAdsL+7u5ldAFwLXB0eal/gYHdftf2XQkREJH4KRkREtl9hzbTWGw68aGaZwAfuPsbM2gPD3H0ygLsvDLetArxiZk0BBzK3VHB4vN+Bp8ysIkHzsHfNbP0mZcKfDYC3zawukAVMjjnMRwpEREQkGdRMS0QkQu4+DDgUmAG8ZmZnA0YQbBR0JzDY3ZsDnYGycRaTG05pwGJ3bxkz7R5u8zjwhLvvBVxU4Ngrtva8REREEkHBiIhIhMxsR2Cuuz8HvAC0An4E2plZk3Cb9c20qhAELQDdt7Ysd18KTDaz/4THNTPbu5Bjn7MNpyIiIpJwCkZERKLVHhhjZqMJ+n886u7zgB7A+2b2K/B2uO39wD1m9j2Qvo3lnQmcHx53HHB8uPw2guZb3wLzt/HYIiIiCWXuhbUUEBERERERiZYyIyIiIiIikhQKRkREREREJCkUjIiIiIiISFIoGBERERERkaRQMCIiIiIiIkmhYERERERERJJCwYiIiIiIiCTF/wP6bDw/6UoUjgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 864x576 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fiscal Year            2021     2022     2023     2024\n",
      "Demographic                                           \n",
      "Accompanied Minors     3024     5985     7482     5906\n",
      "FMUA                 483846   614023   993947   996074\n",
      "Single Adults       1321674  1993694  2061723  1788490\n",
      "UC / Single Minors   147975   152880   137992   110672\n"
     ]
    }
   ],
   "source": [
    "# Visualize the data with a heatmap for the Sum of Encounter Count by Demographic and Fiscal Year.\n",
    "demographic_by_fiscal_year = encounters_aor_df.groupby(['Demographic', 'Fiscal Year'])['Encounter Count'].sum().unstack(fill_value=0)\n",
    "plt.figure(figsize=(12, 8))\n",
    "sns.heatmap(demographic_by_fiscal_year, annot=True, fmt='d', cmap='viridis', cbar_kws={'label': 'Encounter Count'})\n",
    "plt.title('Total Encounters by Demographic and Fiscal Year')\n",
    "plt.xlabel('Fiscal Year')\n",
    "plt.ylabel('Demographic')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "plt.show()\n",
    "\n",
    "print(demographic_by_fiscal_year)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "a5948ba3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fiscal Year            2021     2022     2023     2024  Standard Deviation  \\\n",
      "Demographic                                                                  \n",
      "Accompanied Minors     3024     5985     7482     5906         1863.648639   \n",
      "FMUA                 483846   614023   993947   996074       262969.634182   \n",
      "Single Adults       1321674  1993694  2061723  1788490       333990.204373   \n",
      "UC / Single Minors   147975   152880   137992   110672        18852.018749   \n",
      "\n",
      "Fiscal Year             Variance  \n",
      "Demographic                       \n",
      "Accompanied Minors  3.473186e+06  \n",
      "FMUA                6.915303e+10  \n",
      "Single Adults       1.115495e+11  \n",
      "UC / Single Minors  3.553986e+08  \n"
     ]
    }
   ],
   "source": [
    "# Calculate the standard deviation and variance of the Sum of Encounter Count by Citizenship and Fiscal Year. \n",
    "demographic_by_fiscal_year = encounters_aor_df.groupby(['Demographic', 'Fiscal Year'])['Encounter Count'].sum().unstack(fill_value=0)\n",
    "demographic_by_fiscal_year_stats = demographic_by_fiscal_year.copy()\n",
    "demographic_by_fiscal_year_stats['Standard Deviation'] = demographic_by_fiscal_year.std(axis=1)\n",
    "demographic_by_fiscal_year_stats['Variance'] = demographic_by_fiscal_year.var(axis=1)\n",
    "# Display the updated DataFrame with standard deviation and variance\n",
    "print(demographic_by_fiscal_year_stats)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "0f7509ba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "cells": {
          "align": "left",
          "fill": {
           "color": "lavender"
          },
          "values": [
           [
            "Accompanied Minors",
            "FMUA",
            "Single Adults",
            "UC / Single Minors"
           ],
           [
            3024,
            483846,
            1321674,
            147975
           ],
           [
            5985,
            614023,
            1993694,
            152880
           ],
           [
            7482,
            993947,
            2061723,
            137992
           ],
           [
            5906,
            996074,
            1788490,
            110672
           ],
           [
            1863.65,
            262969.63,
            333990.2,
            18852.02
           ],
           [
            3473186.25,
            69153028501.67,
            111549456616.92,
            355398610.92
           ]
          ]
         },
         "header": {
          "align": "left",
          "fill": {
           "color": "paleturquoise"
          },
          "values": [
           "Demographic",
           "2021",
           "2022",
           "2023",
           "2024",
           "Standard Deviation",
           "Variance"
          ]
         },
         "type": "table"
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Encounter Count by Demographic and Fiscal Year (with Statistics)"
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import plotly.graph_objects as go\n",
    "\n",
    "# Prepare data for the table\n",
    "table = go.Figure(data=[go.Table(\n",
    "    header=dict(values=[\"Demographic\", \"2021\", \"2022\", \"2023\", \"2024\", \"Standard Deviation\", \"Variance\"],\n",
    "                fill_color='paleturquoise',\n",
    "                align='left'),\n",
    "    cells=dict(values=[\n",
    "        demographic_by_fiscal_year_stats.index,  # Citizenship\n",
    "        demographic_by_fiscal_year_stats[2021],\n",
    "        demographic_by_fiscal_year_stats[2022],\n",
    "        demographic_by_fiscal_year_stats[2023],\n",
    "        demographic_by_fiscal_year_stats[2024],\n",
    "        demographic_by_fiscal_year_stats['Standard Deviation'].round(2),\n",
    "        demographic_by_fiscal_year_stats['Variance'].round(2)\n",
    "    ],\n",
    "    fill_color='lavender',\n",
    "    align='left'))\n",
    "])\n",
    "\n",
    "table.update_layout(title='Encounter Count by Demographic and Fiscal Year (with Statistics)')\n",
    "table.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "f6a6dda9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fiscal Year        2021    2022    2023    2024  Standard Deviation  \\\n",
      "Citizenship                                                           \n",
      "BRAZIL            58059   57021   32492   32130        14572.882179   \n",
      "CANADA            22371   47126   44700   45045        11675.614202   \n",
      "CHINA             23471   27756   52700   78701        25522.370462   \n",
      "COLOMBIA          10495  130971  167388  134676        68896.541183   \n",
      "CUBA              39303  224607  200287  217615        88028.972534   \n",
      "ECUADOR           97074   24936  117487  124023        45436.283849   \n",
      "EL SALVADOR       99463   97797   62846   57207        22416.639287   \n",
      "GUATEMALA        284291  233061  221849  206971        33577.833204   \n",
      "HAITI             48727   56596  163781  220798        83969.058009   \n",
      "HONDURAS         321149  214975  216028  144373        72854.470997   \n",
      "INDIA             30662   63927   96917   90415        30137.098548   \n",
      "MEXICO           674739  823057  735937  668088        71877.460706   \n",
      "MYANMAR (BURMA)    3841    4470    4257    5004          483.890483   \n",
      "NICARAGUA         50722  164600  138729   91049        50573.493143   \n",
      "OTHER             57357  137328  299575  267575       113125.629982   \n",
      "PERU               5177   53188   78202   39200        30465.542857   \n",
      "PHILIPPINES       46353   55117   51399   48421         3808.705598   \n",
      "ROMANIA            5159    7411    3692    2548         2098.201214   \n",
      "RUSSIA            13240   36271   57163   21891        19196.073251   \n",
      "TURKEY             4989   19470   18986   13311         6740.698628   \n",
      "UKRAINE            9378   97377  101815   78605        42809.255645   \n",
      "VENEZUELA         50499  189520  334914  313496       131134.265548   \n",
      "\n",
      "Fiscal Year          Variance  \n",
      "Citizenship                    \n",
      "BRAZIL           2.123689e+08  \n",
      "CANADA           1.363200e+08  \n",
      "CHINA            6.513914e+08  \n",
      "COLOMBIA         4.746733e+09  \n",
      "CUBA             7.749100e+09  \n",
      "ECUADOR          2.064456e+09  \n",
      "EL SALVADOR      5.025057e+08  \n",
      "GUATEMALA        1.127471e+09  \n",
      "HAITI            7.050803e+09  \n",
      "HONDURAS         5.307774e+09  \n",
      "INDIA            9.082447e+08  \n",
      "MEXICO           5.166369e+09  \n",
      "MYANMAR (BURMA)  2.341500e+05  \n",
      "NICARAGUA        2.557678e+09  \n",
      "OTHER            1.279741e+10  \n",
      "PERU             9.281493e+08  \n",
      "PHILIPPINES      1.450624e+07  \n",
      "ROMANIA          4.402448e+06  \n",
      "RUSSIA           3.684892e+08  \n",
      "TURKEY           4.543702e+07  \n",
      "UKRAINE          1.832632e+09  \n",
      "VENEZUELA        1.719620e+10  \n"
     ]
    }
   ],
   "source": [
    "# Calculate the standard deviation and variance of the Sum of Encounter Count by Citizenship and Fiscal Year. \n",
    "citizenship_by_fiscal_year = encounters_aor_df.groupby(['Citizenship', 'Fiscal Year'])['Encounter Count'].sum().unstack(fill_value=0)\n",
    "citizenship_by_fiscal_year_stats = citizenship_by_fiscal_year.copy()\n",
    "citizenship_by_fiscal_year_stats['Standard Deviation'] = citizenship_by_fiscal_year.std(axis=1)\n",
    "citizenship_by_fiscal_year_stats['Variance'] = citizenship_by_fiscal_year.var(axis=1)\n",
    "# Display the updated DataFrame with standard deviation and variance\n",
    "print(citizenship_by_fiscal_year_stats)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "fe9c54f4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "cells": {
          "align": "left",
          "fill": {
           "color": "lavender"
          },
          "values": [
           [
            "BRAZIL",
            "CANADA",
            "CHINA",
            "COLOMBIA",
            "CUBA",
            "ECUADOR",
            "EL SALVADOR",
            "GUATEMALA",
            "HAITI",
            "HONDURAS",
            "INDIA",
            "MEXICO",
            "MYANMAR (BURMA)",
            "NICARAGUA",
            "OTHER",
            "PERU",
            "PHILIPPINES",
            "ROMANIA",
            "RUSSIA",
            "TURKEY",
            "UKRAINE",
            "VENEZUELA"
           ],
           [
            58059,
            22371,
            23471,
            10495,
            39303,
            97074,
            99463,
            284291,
            48727,
            321149,
            30662,
            674739,
            3841,
            50722,
            57357,
            5177,
            46353,
            5159,
            13240,
            4989,
            9378,
            50499
           ],
           [
            57021,
            47126,
            27756,
            130971,
            224607,
            24936,
            97797,
            233061,
            56596,
            214975,
            63927,
            823057,
            4470,
            164600,
            137328,
            53188,
            55117,
            7411,
            36271,
            19470,
            97377,
            189520
           ],
           [
            32492,
            44700,
            52700,
            167388,
            200287,
            117487,
            62846,
            221849,
            163781,
            216028,
            96917,
            735937,
            4257,
            138729,
            299575,
            78202,
            51399,
            3692,
            57163,
            18986,
            101815,
            334914
           ],
           [
            32130,
            45045,
            78701,
            134676,
            217615,
            124023,
            57207,
            206971,
            220798,
            144373,
            90415,
            668088,
            5004,
            91049,
            267575,
            39200,
            48421,
            2548,
            21891,
            13311,
            78605,
            313496
           ],
           [
            14572.88,
            11675.61,
            25522.37,
            68896.54,
            88028.97,
            45436.28,
            22416.64,
            33577.83,
            83969.06,
            72854.47,
            30137.1,
            71877.46,
            483.89,
            50573.49,
            113125.63,
            30465.54,
            3808.71,
            2098.2,
            19196.07,
            6740.7,
            42809.26,
            131134.27
           ],
           [
            212368895,
            136319967,
            651391394,
            4746733387,
            7749100005.33,
            2064455890,
            502505716.92,
            1127470882.67,
            7050802703,
            5307773944.25,
            908244708.92,
            5166369357.58,
            234150,
            2557678208.67,
            12797408158.92,
            928149301.58,
            14506238.33,
            4402448.33,
            368489228.25,
            45437018,
            1832632368.92,
            17196195600.92
           ]
          ]
         },
         "header": {
          "align": "left",
          "fill": {
           "color": "paleturquoise"
          },
          "values": [
           "Citizenship",
           "2021",
           "2022",
           "2023",
           "2024",
           "Standard Deviation",
           "Variance"
          ]
         },
         "type": "table"
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Encounter Count by Citizenship and Fiscal Year (with Statistics)"
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import plotly.graph_objects as go\n",
    "\n",
    "# Prepare data for the table\n",
    "table = go.Figure(data=[go.Table(\n",
    "    header=dict(values=[\"Citizenship\", \"2021\", \"2022\", \"2023\", \"2024\", \"Standard Deviation\", \"Variance\"],\n",
    "                fill_color='paleturquoise',\n",
    "                align='left'),\n",
    "    cells=dict(values=[\n",
    "        citizenship_by_fiscal_year_stats.index,  # Citizenship\n",
    "        citizenship_by_fiscal_year_stats[2021],\n",
    "        citizenship_by_fiscal_year_stats[2022],\n",
    "        citizenship_by_fiscal_year_stats[2023],\n",
    "        citizenship_by_fiscal_year_stats[2024],\n",
    "        citizenship_by_fiscal_year_stats['Standard Deviation'].round(2),\n",
    "        citizenship_by_fiscal_year_stats['Variance'].round(2)\n",
    "    ],\n",
    "    fill_color='lavender',\n",
    "    align='left'))\n",
    "])\n",
    "\n",
    "table.update_layout(title='Encounter Count by Citizenship and Fiscal Year (with Statistics)')\n",
    "table.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "d0a9c9a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "Citizenship=BRAZIL<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "BRAZIL",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "BRAZIL",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          58059,
          57021,
          32492,
          32130
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=CANADA<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "CANADA",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "CANADA",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          22371,
          47126,
          44700,
          45045
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=CHINA<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "CHINA",
         "line": {
          "color": "#00cc96",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "CHINA",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          23471,
          27756,
          52700,
          78701
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=COLOMBIA<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "COLOMBIA",
         "line": {
          "color": "#ab63fa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "COLOMBIA",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          10495,
          130971,
          167388,
          134676
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=CUBA<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "CUBA",
         "line": {
          "color": "#FFA15A",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "CUBA",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          39303,
          224607,
          200287,
          217615
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=ECUADOR<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "ECUADOR",
         "line": {
          "color": "#19d3f3",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "ECUADOR",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          97074,
          24936,
          117487,
          124023
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=EL SALVADOR<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "EL SALVADOR",
         "line": {
          "color": "#FF6692",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "EL SALVADOR",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          99463,
          97797,
          62846,
          57207
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=GUATEMALA<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "GUATEMALA",
         "line": {
          "color": "#B6E880",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "GUATEMALA",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          284291,
          233061,
          221849,
          206971
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=HAITI<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "HAITI",
         "line": {
          "color": "#FF97FF",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "HAITI",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          48727,
          56596,
          163781,
          220798
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=HONDURAS<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "HONDURAS",
         "line": {
          "color": "#FECB52",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "HONDURAS",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          321149,
          214975,
          216028,
          144373
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=INDIA<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "INDIA",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "INDIA",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          30662,
          63927,
          96917,
          90415
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=MEXICO<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "MEXICO",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "MEXICO",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          674739,
          823057,
          735937,
          668088
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=MYANMAR (BURMA)<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "MYANMAR (BURMA)",
         "line": {
          "color": "#00cc96",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "MYANMAR (BURMA)",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          3841,
          4470,
          4257,
          5004
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=NICARAGUA<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "NICARAGUA",
         "line": {
          "color": "#ab63fa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "NICARAGUA",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          50722,
          164600,
          138729,
          91049
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=OTHER<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "OTHER",
         "line": {
          "color": "#FFA15A",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "OTHER",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          57357,
          137328,
          299575,
          267575
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=PERU<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "PERU",
         "line": {
          "color": "#19d3f3",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "PERU",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          5177,
          53188,
          78202,
          39200
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=PHILIPPINES<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "PHILIPPINES",
         "line": {
          "color": "#FF6692",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "PHILIPPINES",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          46353,
          55117,
          51399,
          48421
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=ROMANIA<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "ROMANIA",
         "line": {
          "color": "#B6E880",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "ROMANIA",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          5159,
          7411,
          3692,
          2548
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=RUSSIA<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "RUSSIA",
         "line": {
          "color": "#FF97FF",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "RUSSIA",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          13240,
          36271,
          57163,
          21891
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=TURKEY<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "TURKEY",
         "line": {
          "color": "#FECB52",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "TURKEY",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          4989,
          19470,
          18986,
          13311
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=UKRAINE<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "UKRAINE",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "UKRAINE",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          9378,
          97377,
          101815,
          78605
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Citizenship=VENEZUELA<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "VENEZUELA",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "VENEZUELA",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          50499,
          189520,
          334914,
          313496
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "legend": {
         "title": {
          "text": "Citizenship"
         },
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Trend Line of Total Encounters by Citizenship and Fiscal Year"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Fiscal Year FY21-FY24"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Total Encounters"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create visualization of data over time for the Sum of Encounter Count by Citizenship and Fiscal Year. Add interactive table with plotly. Add trend line to the table.\n",
    "fig = px.line(citizenship_by_fiscal_year.reset_index().melt(id_vars='Citizenship', var_name='Fiscal Year', value_name='Encounter Count'),\n",
    "              x='Fiscal Year', y='Encounter Count', color='Citizenship',\n",
    "              title='Trend Line of Total Encounters by Citizenship and Fiscal Year',\n",
    "              labels={'Encounter Count': 'Total Encounters', 'Citizenship': 'Citizenship'})\n",
    "fig.update_traces(mode='lines+markers')\n",
    "fig.update_layout(yaxis_title='Total Encounters', xaxis_title='Fiscal Year FY21-FY24')\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "77de29a0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "Fiscal Year=2021<br>Month=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "2021",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "2021",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "APR",
          "AUG",
          "DEC",
          "FEB",
          "JAN",
          "JUL",
          "JUN",
          "MAR",
          "MAY",
          "NOV",
          "OCT",
          "SEP"
         ],
         "xaxis": "x",
         "y": [
          1801,
          1827,
          1882,
          1450,
          2183,
          2004,
          1868,
          1881,
          1903,
          2433,
          2275,
          1964
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Fiscal Year=2022<br>Month=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "2022",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "2022",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "APR",
          "AUG",
          "DEC",
          "FEB",
          "JAN",
          "JUL",
          "JUN",
          "MAR",
          "MAY",
          "NOV",
          "OCT",
          "SEP"
         ],
         "xaxis": "x",
         "y": [
          2096,
          2465,
          2634,
          2289,
          2699,
          2191,
          2472,
          1990,
          2036,
          2186,
          2188,
          2510
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Fiscal Year=2023<br>Month=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "2023",
         "line": {
          "color": "#00cc96",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "2023",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "APR",
          "AUG",
          "DEC",
          "FEB",
          "JAN",
          "JUL",
          "JUN",
          "MAR",
          "MAY",
          "NOV",
          "OCT",
          "SEP"
         ],
         "xaxis": "x",
         "y": [
          5434,
          5864,
          2818,
          3150,
          3147,
          6157,
          4601,
          4437,
          5172,
          2368,
          2281,
          7271
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Fiscal Year=2024<br>Month=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "2024",
         "line": {
          "color": "#ab63fa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "2024",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "APR",
          "AUG",
          "DEC",
          "FEB",
          "JAN",
          "JUL",
          "JUN",
          "MAR",
          "MAY",
          "NOV",
          "OCT",
          "SEP"
         ],
         "xaxis": "x",
         "y": [
          6527,
          6040,
          8615,
          7112,
          6772,
          5569,
          6171,
          5069,
          7421,
          7238,
          7160,
          5007
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "legend": {
         "title": {
          "text": "Fiscal Year"
         },
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Trend Line of Total Encounters by Fiscal Year and Month for Citizenship: CHINA"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Month"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Total Encounters"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create a trend line graph for the Sum of Encounter by Fiscal Year and Month for Citizenship == 'CHINA'. Add sum of Encounter Count to the table.\n",
    "china_encounters = encounters_aor_df[encounters_aor_df['Citizenship'] == 'CHINA']\n",
    "china_encounters_by_year_month = china_encounters.groupby(['Fiscal Year', 'Month'])['Encounter Count'].sum().unstack(fill_value=0)  \n",
    "fig = px.line(china_encounters_by_year_month.reset_index().melt(id_vars='Fiscal Year', var_name='Month', value_name='Encounter Count'),\n",
    "              x='Month', y='Encounter Count', color='Fiscal Year',\n",
    "              title='Trend Line of Total Encounters by Fiscal Year and Month for Citizenship: CHINA',\n",
    "              labels={'Encounter Count': 'Total Encounters', 'Month': 'Month'})\n",
    "fig.update_traces(mode='lines+markers')\n",
    "fig.update_layout(yaxis_title='Total Encounters', xaxis_title='Month')\n",
    "fig.show()  \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "5ae7555b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "cells": {
          "align": "left",
          "fill": {
           "color": "lavender"
          },
          "values": [
           [
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024
           ],
           [
            "APR",
            "AUG",
            "DEC",
            "FEB",
            "JAN",
            "JUL",
            "JUN",
            "MAR",
            "MAY",
            "NOV",
            "OCT",
            "SEP",
            "APR",
            "AUG",
            "DEC",
            "FEB",
            "JAN",
            "JUL",
            "JUN",
            "MAR",
            "MAY",
            "NOV",
            "OCT",
            "SEP",
            "APR",
            "AUG",
            "DEC",
            "FEB",
            "JAN",
            "JUL",
            "JUN",
            "MAR",
            "MAY",
            "NOV",
            "OCT",
            "SEP",
            "APR",
            "AUG",
            "DEC",
            "FEB",
            "JAN",
            "JUL",
            "JUN",
            "MAR",
            "MAY",
            "NOV",
            "OCT",
            "SEP"
           ],
           [
            1801,
            1827,
            1882,
            1450,
            2183,
            2004,
            1868,
            1881,
            1903,
            2433,
            2275,
            1964,
            2096,
            2465,
            2634,
            2289,
            2699,
            2191,
            2472,
            1990,
            2036,
            2186,
            2188,
            2510,
            5434,
            5864,
            2818,
            3150,
            3147,
            6157,
            4601,
            4437,
            5172,
            2368,
            2281,
            7271,
            6527,
            6040,
            8615,
            7112,
            6772,
            5569,
            6171,
            5069,
            7421,
            7238,
            7160,
            5007
           ],
           [
            52.97,
            46.85,
            57.03,
            51.79,
            80.85,
            48.88,
            54.94,
            64.86,
            61.39,
            86.89,
            66.91,
            41.79,
            45.57,
            45.65,
            50.65,
            54.5,
            71.03,
            45.65,
            57.49,
            52.37,
            49.66,
            52.05,
            60.78,
            55.78,
            83.6,
            96.13,
            53.17,
            53.39,
            56.2,
            100.93,
            85.2,
            72.74,
            83.42,
            49.33,
            48.53,
            123.24,
            123.15,
            97.42,
            156.64,
            139.45,
            144.09,
            103.13,
            114.28,
            97.48,
            137.43,
            157.35,
            146.12,
            108.85
           ],
           [
            4.5,
            8,
            5,
            17.5,
            10,
            6,
            15.5,
            11,
            7,
            5,
            3.5,
            6,
            10,
            10.5,
            5,
            6.5,
            14,
            9,
            20,
            15,
            23,
            6,
            12.5,
            9,
            9,
            8,
            10,
            11,
            10,
            9,
            10.5,
            13,
            4.5,
            10,
            12,
            7,
            9,
            9,
            11,
            11,
            18,
            9.5,
            11,
            8.5,
            10,
            12.5,
            13,
            10.5
           ],
           [
            100.55,
            92.29,
            139.91,
            85.5,
            153.7,
            108.25,
            95.65,
            113.74,
            124.81,
            198.88,
            174.87,
            89.71,
            80.09,
            77.83,
            102.98,
            102.56,
            127.08,
            75.08,
            84.92,
            90.7,
            75.74,
            100.33,
            113.21,
            100.95,
            277.52,
            276.89,
            92.43,
            104.34,
            112.07,
            285.9,
            169.73,
            185.48,
            223.59,
            87.62,
            82.93,
            464.14,
            411.37,
            227.99,
            700.63,
            415.59,
            473.26,
            241.49,
            324.02,
            253.69,
            445.05,
            632.84,
            540.66,
            250.96
           ],
           [
            10110.64,
            8517.55,
            19574.53,
            7309.95,
            23625.13,
            11718.16,
            9149.33,
            12937.27,
            15578.58,
            39551.73,
            30579.9,
            8048.56,
            6413.94,
            6057.74,
            10605.41,
            10519.48,
            16148.62,
            5637.21,
            7211.35,
            8226.35,
            5736.68,
            10065.51,
            12815.61,
            10191.36,
            77015.15,
            76665.32,
            8543.87,
            10886.86,
            12559.36,
            81740,
            28807.83,
            34402.9,
            49991.17,
            7677.25,
            6877.12,
            215427.18,
            169223.78,
            51977.23,
            490875.79,
            172716.13,
            223973.56,
            58316.34,
            104990.2,
            64359.39,
            198072.59,
            400484.19,
            292313.73,
            62979.95
           ],
           [
            393,
            408,
            730,
            341,
            620,
            481,
            376,
            439,
            522,
            914,
            957,
            482,
            390,
            313,
            441,
            488,
            535,
            318,
            370,
            472,
            292,
            387,
            439,
            538,
            2136,
            1963,
            415,
            583,
            600,
            2015,
            952,
            1324,
            1530,
            415,
            358,
            3429,
            2731,
            1057,
            5170,
            2773,
            3177,
            1270,
            1772,
            1490,
            2848,
            4282,
            3672,
            1336
           ],
           [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1
           ]
          ]
         },
         "header": {
          "align": "left",
          "fill": {
           "color": "paleturquoise"
          },
          "values": [
           "Fiscal Year",
           "Month",
           "Sum",
           "Mean",
           "Median",
           "Standard Deviation",
           "Variance",
           "Max",
           "Min"
          ]
         },
         "type": "table"
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Encounter Count Statistics for Citizenship: CHINA by Fiscal Year and Month"
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Create a statistics table for the Sum of Encounter Count by Fiscal Year and Month for Citizenship == 'CHINA'. Add mean, median, standard deviation, variance, max, min to the table.\n",
    "china_encounters_stats = china_encounters.groupby(['Fiscal Year', 'Month'])['Encounter Count'].agg(['sum', 'mean', 'median', 'std', 'var', 'max', 'min']).reset_index()\n",
    "china_encounters_stats.columns = ['Fiscal Year', 'Month', 'Sum', 'Mean', 'Median', 'Standard Deviation', 'Variance', 'Max', 'Min']\n",
    "import plotly.graph_objects as go\n",
    "# Prepare data for the table\n",
    "table = go.Figure(data=[go.Table(\n",
    "    header=dict(values=[\"Fiscal Year\", \"Month\", \"Sum\", \"Mean\", \"Median\", \"Standard Deviation\", \"Variance\", \"Max\", \"Min\"],\n",
    "                fill_color='paleturquoise',\n",
    "                align='left'),\n",
    "    cells=dict(values=[\n",
    "        china_encounters_stats['Fiscal Year'],  # Fiscal Year\n",
    "        china_encounters_stats['Month'],  # Month\n",
    "        china_encounters_stats['Sum'],  # Sum\n",
    "        china_encounters_stats['Mean'].round(2),  # Mean\n",
    "        china_encounters_stats['Median'].round(2),  # Median\n",
    "        china_encounters_stats['Standard Deviation'].round(2),  # Standard Deviation\n",
    "        china_encounters_stats['Variance'].round(2),  # Variance\n",
    "        china_encounters_stats['Max'],  # Max\n",
    "        china_encounters_stats['Min']  # Min\n",
    "    ],\n",
    "    fill_color='lavender',\n",
    "    align='left'))\n",
    "])\n",
    "table.update_layout(title='Encounter Count Statistics for Citizenship: CHINA by Fiscal Year and Month')\n",
    "table.show()\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "ad5ee375",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Demographic\n",
      "Accompanied Minors       624\n",
      "FMUA                   21126\n",
      "Single Adults         160597\n",
      "UC / Single Minors       281\n",
      "Name: Encounter Count, dtype: int64\n"
     ]
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "cells": {
          "align": "left",
          "fill": {
           "color": "lavender"
          },
          "values": [
           [
            "Accompanied Minors",
            "FMUA",
            "Single Adults",
            "UC / Single Minors"
           ],
           [
            624,
            21126,
            160597,
            281
           ]
          ]
         },
         "header": {
          "align": "left",
          "fill": {
           "color": "paleturquoise"
          },
          "values": [
           "Demographic",
           "Total Encounters"
          ]
         },
         "type": "table"
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Total Encounters by Demographic for Citizenship: CHINA"
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "china_encounters_by_demographic = encounters_aor_df[encounters_aor_df['Citizenship'] == 'CHINA'].groupby('Demographic')['Encounter Count'].sum()\n",
    "print(china_encounters_by_demographic)\n",
    "\n",
    "# Table with results.\n",
    "import plotly.graph_objects as go\n",
    "# Prepare data for the table\n",
    "table = go.Figure(data=[go.Table(\n",
    "    header=dict(values=[\"Demographic\", \"Total Encounters\"],     \n",
    "                fill_color='paleturquoise',\n",
    "                align='left'),\n",
    "    cells=dict(values=[\n",
    "        china_encounters_by_demographic.index,  # Demographic   \n",
    "        china_encounters_by_demographic.values  # Total Encounters\n",
    "    ],\n",
    "    fill_color='lavender',\n",
    "    align='left'))\n",
    "])\n",
    "table.update_layout(title='Total Encounters by Demographic for Citizenship: CHINA')\n",
    "table.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "0fb342cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "Fiscal Year=2021<br>Month=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "2021",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "2021",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "APR",
          "AUG",
          "DEC",
          "FEB",
          "JAN",
          "JUL",
          "JUN",
          "MAR",
          "MAY",
          "NOV",
          "OCT",
          "SEP"
         ],
         "xaxis": "x",
         "y": [
          889,
          1727,
          722,
          720,
          790,
          1559,
          1245,
          897,
          1069,
          691,
          469,
          2462
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Fiscal Year=2022<br>Month=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "2022",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "2022",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "APR",
          "AUG",
          "DEC",
          "FEB",
          "JAN",
          "JUL",
          "JUN",
          "MAR",
          "MAY",
          "NOV",
          "OCT",
          "SEP"
         ],
         "xaxis": "x",
         "y": [
          2867,
          2891,
          3406,
          2024,
          2620,
          2899,
          3122,
          2623,
          4354,
          3032,
          2725,
          3708
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Fiscal Year=2023<br>Month=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "2023",
         "line": {
          "color": "#00cc96",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "2023",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "APR",
          "AUG",
          "DEC",
          "FEB",
          "JAN",
          "JUL",
          "JUN",
          "MAR",
          "MAY",
          "NOV",
          "OCT",
          "SEP"
         ],
         "xaxis": "x",
         "y": [
          3633,
          2874,
          9227,
          5886,
          5805,
          2972,
          2349,
          5273,
          4133,
          6931,
          5174,
          2906
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Fiscal Year=2024<br>Month=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "2024",
         "line": {
          "color": "#ab63fa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "2024",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "APR",
          "AUG",
          "DEC",
          "FEB",
          "JAN",
          "JUL",
          "JUN",
          "MAR",
          "MAY",
          "NOV",
          "OCT",
          "SEP"
         ],
         "xaxis": "x",
         "y": [
          1587,
          1129,
          3015,
          1877,
          2295,
          1344,
          1087,
          1569,
          1395,
          2506,
          2935,
          1152
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "legend": {
         "title": {
          "text": "Fiscal Year"
         },
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Trend Line of Total Encounters by Month for Citizenship: RUSSIA"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Month"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Total Encounters"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create a trend line graph for the Sum of Encounter by Fiscal Year and Month for Citizenship == 'Russia'. Add sum of Encounter Count to the table.\n",
    "russia_encounters = encounters_aor_df[encounters_aor_df['Citizenship'] == 'RUSSIA']\n",
    "russia_encounters_by_year_month = russia_encounters.groupby(['Fiscal Year', 'Month'])['Encounter Count'].sum().unstack(fill_value=0)\n",
    "fig = px.line(russia_encounters_by_year_month.reset_index().melt(id_vars='Fiscal Year', var_name='Month', value_name='Encounter Count'),\n",
    "              x='Month', y='Encounter Count', color='Fiscal Year',\n",
    "              title='Trend Line of Total Encounters by Month for Citizenship: RUSSIA',\n",
    "              labels={'Encounter Count': 'Total Encounters', 'Month': 'Month'})\n",
    "fig.update_traces(mode='lines+markers')\n",
    "fig.update_layout(yaxis_title='Total Encounters', xaxis_title='Month')\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "25beddd2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "cells": {
          "align": "left",
          "fill": {
           "color": "lavender"
          },
          "values": [
           [
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024
           ],
           [
            "APR",
            "AUG",
            "DEC",
            "FEB",
            "JAN",
            "JUL",
            "JUN",
            "MAR",
            "MAY",
            "NOV",
            "OCT",
            "SEP",
            "APR",
            "AUG",
            "DEC",
            "FEB",
            "JAN",
            "JUL",
            "JUN",
            "MAR",
            "MAY",
            "NOV",
            "OCT",
            "SEP",
            "APR",
            "AUG",
            "DEC",
            "FEB",
            "JAN",
            "JUL",
            "JUN",
            "MAR",
            "MAY",
            "NOV",
            "OCT",
            "SEP",
            "APR",
            "AUG",
            "DEC",
            "FEB",
            "JAN",
            "JUL",
            "JUN",
            "MAR",
            "MAY",
            "NOV",
            "OCT",
            "SEP"
           ],
           [
            889,
            1727,
            722,
            720,
            790,
            1559,
            1245,
            897,
            1069,
            691,
            469,
            2462,
            2867,
            2891,
            3406,
            2024,
            2620,
            2899,
            3122,
            2623,
            4354,
            3032,
            2725,
            3708,
            3633,
            2874,
            9227,
            5886,
            5805,
            2972,
            2349,
            5273,
            4133,
            6931,
            5174,
            2906,
            1587,
            1129,
            3015,
            1877,
            2295,
            1344,
            1087,
            1569,
            1395,
            2506,
            2935,
            1152
           ],
           [
            31.75,
            46.68,
            30.08,
            31.3,
            34.35,
            47.24,
            34.58,
            34.5,
            39.59,
            27.64,
            22.33,
            70.34,
            56.22,
            59,
            94.61,
            56.22,
            77.06,
            53.69,
            58.91,
            63.98,
            85.37,
            89.18,
            71.71,
            67.42,
            68.55,
            63.87,
            141.95,
            105.11,
            107.5,
            69.12,
            53.39,
            101.4,
            81.04,
            117.47,
            94.07,
            66.05,
            38.71,
            32.26,
            77.31,
            48.13,
            63.75,
            28.6,
            25.88,
            38.27,
            36.71,
            75.94,
            58.7,
            28.8
           ],
           [
            11,
            14,
            10.5,
            12,
            11,
            11,
            10,
            10.5,
            12,
            8,
            16,
            11,
            7,
            12,
            16,
            12,
            18.5,
            6,
            8,
            7,
            10,
            11,
            6,
            8,
            5,
            8,
            8,
            8.5,
            9.5,
            7,
            11,
            10,
            13,
            9,
            11,
            10,
            10,
            9,
            12,
            11,
            14,
            5,
            5,
            9,
            11,
            19,
            4.5,
            6.5
           ],
           [
            52.7,
            88.53,
            54.14,
            41.02,
            58.46,
            88.36,
            53.16,
            48.76,
            57.76,
            50.96,
            34.9,
            158.84,
            156.79,
            135.1,
            221.27,
            98.57,
            133.17,
            121.49,
            141.57,
            129.07,
            241.55,
            201.05,
            177.23,
            186.36,
            177.31,
            187.76,
            362.49,
            295.52,
            240.29,
            169.33,
            119.64,
            261.61,
            192.64,
            362.79,
            280.7,
            158.74,
            79.42,
            57.61,
            168.82,
            93.83,
            109.95,
            63.82,
            57.76,
            67.11,
            76.83,
            136.14,
            152.42,
            61.85
           ],
           [
            2777.53,
            7837.61,
            2931.04,
            1682.49,
            3417.78,
            7808.31,
            2825.68,
            2377.46,
            3336.17,
            2596.49,
            1217.93,
            25229.23,
            24582.17,
            18253,
            48961.56,
            9716.41,
            17734.42,
            14761.01,
            20042.28,
            16659.32,
            58344.92,
            40422.57,
            31410,
            34730.36,
            31437.21,
            35253.85,
            131400.95,
            87330.13,
            57739.58,
            28671.49,
            14312.85,
            68441.19,
            37111.88,
            131615.32,
            78794.33,
            25198.37,
            6307.31,
            3319.26,
            28501.17,
            8804.11,
            12090.02,
            4073.03,
            3336.55,
            4503.65,
            5903.35,
            18534.75,
            23233.03,
            3825.96
           ],
           [
            232,
            333,
            236,
            155,
            263,
            373,
            193,
            166,
            207,
            197,
            154,
            654,
            803,
            658,
            1004,
            399,
            533,
            684,
            803,
            526,
            1387,
            822,
            752,
            1060,
            974,
            1031,
            1949,
            1496,
            1133,
            819,
            591,
            1370,
            827,
            2022,
            1512,
            747,
            415,
            299,
            852,
            402,
            435,
            327,
            294,
            323,
            353,
            589,
            839,
            344
           ],
           [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1
           ]
          ]
         },
         "header": {
          "align": "left",
          "fill": {
           "color": "paleturquoise"
          },
          "values": [
           "Fiscal Year",
           "Month",
           "Sum",
           "Mean",
           "Median",
           "Standard Deviation",
           "Variance",
           "Max",
           "Min"
          ]
         },
         "type": "table"
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Encounter Count Statistics for Citizenship: RUSSIA by Fiscal Year"
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Create a statistics table for the Sum of Encounter Count by Fiscal Year for Citizenship == 'RUSSIA'. Add mean, median, standard deviation, variance, max, min to the table. Do not add month.\n",
    "russia_encounters_stats = russia_encounters.groupby(['Fiscal Year', 'Month'])['Encounter Count'].agg(['sum', 'mean', 'median', 'std', 'var', 'max', 'min']).reset_index()\n",
    "russia_encounters_stats.columns = ['Fiscal Year', 'Month', 'Sum', 'Mean', 'Median', 'Standard Deviation', 'Variance', 'Max', 'Min']\n",
    "import plotly.graph_objects as go\n",
    "# Prepare data for the table\n",
    "table = go.Figure(data=[go.Table(\n",
    "    header=dict(values=[\"Fiscal Year\", \"Month\", \"Sum\", \"Mean\", \"Median\", \"Standard Deviation\", \"Variance\", \"Max\", \"Min\"],\n",
    "                fill_color='paleturquoise',\n",
    "                align='left'),\n",
    "    cells=dict(values=[\n",
    "        russia_encounters_stats['Fiscal Year'],  # Fiscal Year\n",
    "        russia_encounters_stats['Month'],  # Month\n",
    "        russia_encounters_stats['Sum'],  # Sum\n",
    "        russia_encounters_stats['Mean'].round(2),  # Mean\n",
    "        russia_encounters_stats['Median'].round(2),  # Median\n",
    "        russia_encounters_stats['Standard Deviation'].round(2),  # Standard Deviation\n",
    "        russia_encounters_stats['Variance'].round(2),  # Variance\n",
    "        russia_encounters_stats['Max'],  # Max\n",
    "        russia_encounters_stats['Min']  # Min\n",
    "    ],\n",
    "    fill_color='lavender',\n",
    "    align='left'))\n",
    "])\n",
    "table.update_layout(title='Encounter Count Statistics for Citizenship: RUSSIA by Fiscal Year')\n",
    "table.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "6a64175f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Demographic\n",
      "Accompanied Minors      144\n",
      "FMUA                  47615\n",
      "Single Adults         80619\n",
      "UC / Single Minors      187\n",
      "Name: Encounter Count, dtype: int64\n"
     ]
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "cells": {
          "align": "left",
          "fill": {
           "color": "lavender"
          },
          "values": [
           [
            "Accompanied Minors",
            "FMUA",
            "Single Adults",
            "UC / Single Minors"
           ],
           [
            144,
            47615,
            80619,
            187
           ]
          ]
         },
         "header": {
          "align": "left",
          "fill": {
           "color": "paleturquoise"
          },
          "values": [
           "Demographic",
           "Total Encounters"
          ]
         },
         "type": "table"
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Total Encounters by Demographic for Citizenship: RUSSIA"
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "russia_encounters_by_demographic = encounters_aor_df[encounters_aor_df['Citizenship'] == 'RUSSIA'].groupby('Demographic')['Encounter Count'].sum()\n",
    "print(russia_encounters_by_demographic)\n",
    "\n",
    "# Table with results.\n",
    "import plotly.graph_objects as go\n",
    "# Prepare data for the table\n",
    "table = go.Figure(data=[go.Table(\n",
    "    header=dict(values=[\"Demographic\", \"Total Encounters\"],     \n",
    "                fill_color='paleturquoise',\n",
    "                align='left'),\n",
    "    cells=dict(values=[\n",
    "        russia_encounters_by_demographic.index,  # Demographic   \n",
    "        russia_encounters_by_demographic.values  # Total Encounters\n",
    "    ],\n",
    "    fill_color='lavender',\n",
    "    align='left'))\n",
    "])\n",
    "table.update_layout(title='Total Encounters by Demographic for Citizenship: RUSSIA')\n",
    "table.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "9aad86d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "Fiscal Year=2021<br>Month=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "2021",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "2021",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "APR",
          "AUG",
          "DEC",
          "FEB",
          "JAN",
          "JUL",
          "JUN",
          "MAR",
          "MAY",
          "NOV",
          "OCT",
          "SEP"
         ],
         "xaxis": "x",
         "y": [
          6172,
          6436,
          371,
          1085,
          459,
          6256,
          7728,
          2740,
          7662,
          386,
          265,
          10939
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Fiscal Year=2022<br>Month=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "2022",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "2022",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "APR",
          "AUG",
          "DEC",
          "FEB",
          "JAN",
          "JUL",
          "JUN",
          "MAR",
          "MAY",
          "NOV",
          "OCT",
          "SEP"
         ],
         "xaxis": "x",
         "y": [
          4281,
          25532,
          24946,
          3225,
          22884,
          17811,
          13355,
          4183,
          5279,
          20549,
          13514,
          33961
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Fiscal Year=2023<br>Month=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "2023",
         "line": {
          "color": "#00cc96",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "2023",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "APR",
          "AUG",
          "DEC",
          "FEB",
          "JAN",
          "JUL",
          "JUN",
          "MAR",
          "MAY",
          "NOV",
          "OCT",
          "SEP"
         ],
         "xaxis": "x",
         "y": [
          40765,
          37908,
          13676,
          13779,
          14946,
          24002,
          26795,
          15992,
          38396,
          13644,
          22686,
          72325
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Fiscal Year=2024<br>Month=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "2024",
         "line": {
          "color": "#ab63fa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "2024",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "APR",
          "AUG",
          "DEC",
          "FEB",
          "JAN",
          "JUL",
          "JUN",
          "MAR",
          "MAY",
          "NOV",
          "OCT",
          "SEP"
         ],
         "xaxis": "x",
         "y": [
          23182,
          16800,
          62852,
          14411,
          16505,
          18018,
          17089,
          21383,
          22116,
          39254,
          45939,
          15947
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "legend": {
         "title": {
          "text": "Fiscal Year"
         },
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Trend Line of Total Encounters by Month for Citizenship: Venezuela"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Month"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Total Encounters"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create a trend line graph for the Sum of Encounter by Fiscal Year and Month for Citizenship == 'VENEZUELA'. Add sum of Encounter Count to the table.\n",
    "venezuela_encounters = encounters_aor_df[encounters_aor_df['Citizenship'] == 'VENEZUELA']\n",
    "venezuela_encounters_by_year_month = venezuela_encounters.groupby(['Fiscal Year', 'Month'])['Encounter Count'].sum().unstack(fill_value=0)\n",
    "fig = px.line(venezuela_encounters_by_year_month.reset_index().melt(id_vars='Fiscal Year', var_name='Month', value_name='Encounter Count'),\n",
    "              x='Month', y='Encounter Count', color='Fiscal Year',\n",
    "              title='Trend Line of Total Encounters by Month for Citizenship: Venezuela',\n",
    "              labels={'Encounter Count': 'Total Encounters', 'Month': 'Month'})\n",
    "fig.update_traces(mode='lines+markers')\n",
    "fig.update_layout(yaxis_title='Total Encounters', xaxis_title='Month')\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "87fe725f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "cells": {
          "align": "left",
          "fill": {
           "color": "lavender"
          },
          "values": [
           [
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2021,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2022,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2023,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024,
            2024
           ],
           [
            "APR",
            "AUG",
            "DEC",
            "FEB",
            "JAN",
            "JUL",
            "JUN",
            "MAR",
            "MAY",
            "NOV",
            "OCT",
            "SEP",
            "APR",
            "AUG",
            "DEC",
            "FEB",
            "JAN",
            "JUL",
            "JUN",
            "MAR",
            "MAY",
            "NOV",
            "OCT",
            "SEP",
            "APR",
            "AUG",
            "DEC",
            "FEB",
            "JAN",
            "JUL",
            "JUN",
            "MAR",
            "MAY",
            "NOV",
            "OCT",
            "SEP",
            "APR",
            "AUG",
            "DEC",
            "FEB",
            "JAN",
            "JUL",
            "JUN",
            "MAR",
            "MAY",
            "NOV",
            "OCT",
            "SEP"
           ],
           [
            6172,
            6436,
            371,
            1085,
            459,
            6256,
            7728,
            2740,
            7662,
            386,
            265,
            10939,
            4281,
            25532,
            24946,
            3225,
            22884,
            17811,
            13355,
            4183,
            5279,
            20549,
            13514,
            33961,
            40765,
            37908,
            13676,
            13779,
            14946,
            24002,
            26795,
            15992,
            38396,
            13644,
            22686,
            72325,
            23182,
            16800,
            62852,
            14411,
            16505,
            18018,
            17089,
            21383,
            22116,
            39254,
            45939,
            15947
           ],
           [
            108.28,
            121.43,
            8.43,
            20.87,
            10.2,
            115.85,
            145.81,
            54.8,
            134.42,
            9.41,
            8.28,
            223.24,
            89.19,
            418.56,
            422.81,
            70.11,
            408.64,
            274.02,
            234.3,
            82.02,
            99.6,
            373.62,
            270.28,
            556.74,
            399.66,
            486,
            150.29,
            154.82,
            171.79,
            307.72,
            362.09,
            158.34,
            380.16,
            133.76,
            280.07,
            964.33,
            293.44,
            240,
            775.95,
            194.74,
            206.31,
            240.24,
            221.94,
            267.29,
            283.54,
            503.26,
            546.89,
            224.61
           ],
           [
            6,
            4,
            3,
            3.5,
            4,
            6.5,
            9,
            5,
            6,
            3,
            4.5,
            4,
            5,
            7,
            7,
            5,
            4.5,
            6,
            6,
            3,
            4,
            6,
            3.5,
            7,
            15.5,
            29.5,
            17,
            9,
            15,
            24.5,
            22.5,
            10,
            21,
            15,
            13,
            33,
            14,
            14.5,
            21,
            18.5,
            12.5,
            15,
            14,
            17,
            22.5,
            17.5,
            17.5,
            8
           ],
           [
            335.71,
            405.27,
            13.27,
            43.54,
            14.44,
            386.68,
            484.32,
            130.91,
            507.7,
            15.83,
            12.04,
            680.36,
            314.31,
            1815.89,
            1330.32,
            210.83,
            1330.64,
            1318.47,
            1102.66,
            304.93,
            381.01,
            1186.42,
            852.36,
            2243.22,
            1191.94,
            1158.42,
            361.95,
            475.81,
            484.71,
            772.43,
            1001.1,
            445.88,
            1268.63,
            366.66,
            1095.51,
            2723.71,
            741.58,
            674.08,
            2457.35,
            428.02,
            459.23,
            597.4,
            517.67,
            665.48,
            631.64,
            1244.86,
            1457.13,
            675.88
           ],
           [
            112703.49,
            164246.52,
            176.11,
            1896.12,
            208.57,
            149518.17,
            234570.54,
            17137.1,
            257757.68,
            250.6,
            145.05,
            462895.06,
            98791.35,
            3297451.65,
            1769740.15,
            44448.85,
            1770608.96,
            1738352.89,
            1215867.75,
            92984.14,
            145171.67,
            1407597.65,
            726513.92,
            5032047.13,
            1420710.33,
            1341942.34,
            131005.43,
            226392.01,
            234947.58,
            596640.72,
            1002192.25,
            198809.37,
            1609429.23,
            134436.97,
            1200138.49,
            7418597.33,
            549946.22,
            454385.25,
            6038561.62,
            183198.88,
            210895.61,
            356890.08,
            267978.43,
            442857.5,
            398968.95,
            1549684.71,
            2123218.19,
            456813.47
           ],
           [
            1967,
            2069,
            66,
            212,
            62,
            2012,
            2740,
            609,
            3104,
            86,
            57,
            2853,
            1939,
            13168,
            5919,
            1145,
            6120,
            9824,
            7903,
            1933,
            2479,
            5699,
            3730,
            14644,
            7103,
            6686,
            2094,
            3488,
            2674,
            4838,
            5885,
            2929,
            9821,
            2132,
            7913,
            14419,
            4430,
            3629,
            17287,
            2233,
            2046,
            2897,
            2494,
            3641,
            2857,
            6956,
            7837,
            3569
           ],
           [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1
           ]
          ]
         },
         "header": {
          "align": "left",
          "fill": {
           "color": "paleturquoise"
          },
          "values": [
           "Fiscal Year",
           "Month",
           "Sum",
           "Mean",
           "Median",
           "Standard Deviation",
           "Variance",
           "Max",
           "Min"
          ]
         },
         "type": "table"
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Encounter Count Statistics for Citizenship: VENEZUELA by Fiscal Year"
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Create a statistics table for the Sum of Encounter Count by Fiscal Year for Citizenship == 'VENEZUELA'. Add mean, median, standard deviation, variance, max, min to the table. Do not add month.\n",
    "venezuela_encounters_stats = venezuela_encounters.groupby(['Fiscal Year', 'Month'])['Encounter Count'].agg(['sum', 'mean', 'median', 'std', 'var', 'max', 'min']).reset_index()\n",
    "venezuela_encounters_stats.columns = ['Fiscal Year', 'Month', 'Sum', 'Mean', 'Median', 'Standard Deviation', 'Variance', 'Max', 'Min']\n",
    "import plotly.graph_objects as go\n",
    "# Prepare data for the table\n",
    "table = go.Figure(data=[go.Table(\n",
    "    header=dict(values=[\"Fiscal Year\", \"Month\", \"Sum\", \"Mean\", \"Median\", \"Standard Deviation\", \"Variance\", \"Max\", \"Min\"],\n",
    "                fill_color='paleturquoise',\n",
    "                align='left'),\n",
    "    cells=dict(values=[\n",
    "        venezuela_encounters_stats['Fiscal Year'],  # Fiscal Year\n",
    "        venezuela_encounters_stats['Month'],  # Month\n",
    "        venezuela_encounters_stats['Sum'],  # Sum\n",
    "        venezuela_encounters_stats['Mean'].round(2),  # Mean\n",
    "        venezuela_encounters_stats['Median'].round(2),  # Median\n",
    "        venezuela_encounters_stats['Standard Deviation'].round(2),  # Standard Deviation\n",
    "        venezuela_encounters_stats['Variance'].round(2),  # Variance\n",
    "        venezuela_encounters_stats['Max'],  # Max\n",
    "        venezuela_encounters_stats['Min']  # Min\n",
    "    ],\n",
    "    fill_color='lavender',\n",
    "    align='left'))\n",
    "])\n",
    "table.update_layout(title='Encounter Count Statistics for Citizenship: VENEZUELA by Fiscal Year')\n",
    "table.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "a22e42c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Demographic\n",
      "Accompanied Minors       681\n",
      "FMUA                  352367\n",
      "Single Adults         527671\n",
      "UC / Single Minors      7710\n",
      "Name: Encounter Count, dtype: int64\n"
     ]
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "cells": {
          "align": "left",
          "fill": {
           "color": "lavender"
          },
          "values": [
           [
            "Accompanied Minors",
            "FMUA",
            "Single Adults",
            "UC / Single Minors"
           ],
           [
            681,
            352367,
            527671,
            7710
           ]
          ]
         },
         "header": {
          "align": "left",
          "fill": {
           "color": "paleturquoise"
          },
          "values": [
           "Demographic",
           "Total Encounters"
          ]
         },
         "type": "table"
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Total Encounters by Demographic for Citizenship: VENEZUELA"
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "venezuela_encounters_by_demographic = encounters_aor_df[encounters_aor_df['Citizenship'] == 'VENEZUELA'].groupby('Demographic')['Encounter Count'].sum()\n",
    "print(venezuela_encounters_by_demographic)\n",
    "\n",
    "# Table with results.\n",
    "import plotly.graph_objects as go\n",
    "# Prepare data for the table\n",
    "table = go.Figure(data=[go.Table(\n",
    "    header=dict(values=[\"Demographic\", \"Total Encounters\"],     \n",
    "                fill_color='paleturquoise',\n",
    "                align='left'),\n",
    "    cells=dict(values=[\n",
    "        venezuela_encounters_by_demographic.index,  # Demographic   \n",
    "        venezuela_encounters_by_demographic.values  # Total Encounters\n",
    "    ],\n",
    "    fill_color='lavender',\n",
    "    align='left'))\n",
    "])\n",
    "table.update_layout(title='Total Encounters by Demographic for Citizenship: VENEZUELA')\n",
    "table.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "dc43f02c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Month           APR     AUG     DEC     FEB     JAN     JUL     JUN     MAR  \\\n",
      "Fiscal Year                                                                   \n",
      "2021         196190  231243   92746  115559   95276  233919  207823  192025   \n",
      "2022         262109  251521  205691  190578  186808  238929  247523  250404   \n",
      "2023         276036  304073  302392  213911  209151  245154  211457  259471   \n",
      "2024         247929  158893  370883  256071  242530  170180  204932  246505   \n",
      "\n",
      "Month           MAY     NOV     OCT     SEP  \n",
      "Fiscal Year                                  \n",
      "2021         198459   89072   90585  213622  \n",
      "2022         274992  198553  187136  272338  \n",
      "2023         275166  284624  278317  341392  \n",
      "2024         240924  308605  309024  144666  \n"
     ]
    }
   ],
   "source": [
    "print(encounters_by_year_month)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "9eed9c3f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean: 163043.25\n",
      "Median: 194107.50\n",
      "Standard Deviation: 60258.34\n",
      "Variance: 3631067214.93\n"
     ]
    }
   ],
   "source": [
    "monthly_counts_2021 = [196190, 231243, 92746, 115559, 95276, 233919, \n",
    "                       207823, 192025, 198459, 89072, 90585, 213622]\n",
    "\n",
    "mean_val = np.mean(monthly_counts_2021)\n",
    "median_val = np.median(monthly_counts_2021)\n",
    "std_dev_val = np.std(monthly_counts_2021, ddof=1)\n",
    "variance_val = np.var(monthly_counts_2021, ddof=1)\n",
    "print(f\"Mean: {mean_val:.2f}\")\n",
    "print(f\"Median: {median_val:.2f}\")\n",
    "print(f\"Standard Deviation: {std_dev_val:.2f}\")\n",
    "print(f\"Variance: {variance_val:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "368e0092",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean: 230548.5, Median: 243226.0, Standard Deviation: 32847.1585820854, Variance: 1078935826.9166667\n"
     ]
    }
   ],
   "source": [
    "monthly_counts_2022 = [262109, 251521, 205691, 190578, 186808, 238929,\n",
    "                       247523, 250404, 274992, 198553, 187136, 272338]\n",
    "mean_val = np.mean(monthly_counts_2022)\n",
    "median_val = np.median(monthly_counts_2022)\n",
    "std_dev_val = np.std(monthly_counts_2022)\n",
    "variance_val = np.var(monthly_counts_2022)\n",
    "print(f\"Mean: {mean_val}, Median: {median_val}, Standard Deviation: {std_dev_val}, Variance: {variance_val}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "04338aab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean: 266762.0, Median: 275601.0, Standard Deviation: 39297.381988710986, Variance: 1544284231.1666667\n"
     ]
    }
   ],
   "source": [
    "monthly_counts_2023 = [276036, 304073, 302392, 213911, 209151, 245154, 211457, \n",
    "                       259471, 275166, 284624, 278317, 341392]\n",
    "mean_val = np.mean(monthly_counts_2023)\n",
    "median_val = np.median(monthly_counts_2023)\n",
    "std_dev_val = np.std(monthly_counts_2023)\n",
    "variance_val = np.var(monthly_counts_2023)\n",
    "print(f\"Mean: {mean_val}, Median: {median_val}, Standard Deviation: {std_dev_val}, Variance: {variance_val}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "2b109af9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean: 241761.83333333334, Median: 244517.5, Standard Deviation: 63709.16955304699, Variance: 4058858285.1388893\n"
     ]
    }
   ],
   "source": [
    "monthly_counts_2024 = [247929, 158893, 370883, 256071, 242530, 170180,\n",
    "                       204932, 246505, 240924, 308605, 309024, 144666]\n",
    "mean_val = np.mean(monthly_counts_2024)\n",
    "median_val = np.median(monthly_counts_2024)\n",
    "std_dev_val = np.std(monthly_counts_2024)\n",
    "variance_val = np.var(monthly_counts_2024)\n",
    "print(f\"Mean: {mean_val}, Median: {median_val}, Standard Deviation: {std_dev_val}, Variance: {variance_val}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "fa4f5baa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "Demographic=Accompanied Minors<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "Accompanied Minors",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "Accompanied Minors",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          3024,
          5985,
          7482,
          5906
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Demographic=FMUA<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "FMUA",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "FMUA",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          483846,
          614023,
          993947,
          996074
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Demographic=Single Adults<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "Single Adults",
         "line": {
          "color": "#00cc96",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "Single Adults",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          1321674,
          1993694,
          2061723,
          1788490
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Demographic=UC / Single Minors<br>Fiscal Year=%{x}<br>Total Encounters=%{y}<extra></extra>",
         "legendgroup": "UC / Single Minors",
         "line": {
          "color": "#ab63fa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines+markers",
         "name": "UC / Single Minors",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          2021,
          2022,
          2023,
          2024
         ],
         "xaxis": "x",
         "y": [
          147975,
          152880,
          137992,
          110672
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "legend": {
         "title": {
          "text": "Demographic"
         },
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Yearly Trend of Total Encounters by Demographic"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Fiscal Year FY21-FY24"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Total Encounters"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "cells": {
          "align": "left",
          "fill": {
           "color": "lavender"
          },
          "values": [
           [
            2021,
            2022,
            2023,
            2024
           ],
           [
            "Accompanied Minors",
            "FMUA",
            "Single Adults",
            "UC / Single Minors",
            "Mean",
            "Median",
            "Standard Deviation",
            "Variance",
            "Max",
            "Min"
           ],
           [
            3024,
            5985,
            7482,
            5906
           ],
           [
            489129.75,
            691645.5,
            800286,
            725285.5
           ],
           [
            315910.5,
            383451.5,
            565969.5,
            553373
           ],
           [
            590435.77,
            905861.31,
            947962.62,
            836458.18
           ],
           [
            348614403284.25,
            820584711369.67,
            898633137580.67,
            699662279985
           ],
           [
            1321674,
            1993694,
            2061723,
            1788490
           ],
           [
            3024,
            5985,
            7482,
            5906
           ]
          ]
         },
         "header": {
          "align": "left",
          "fill": {
           "color": "paleturquoise"
          },
          "values": [
           "Fiscal Year",
           "Demographic",
           "Sum",
           "Mean",
           "Median",
           "Standard Deviation",
           "Variance",
           "Max",
           "Min"
          ]
         },
         "type": "table"
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Encounter Count Statistics by Fiscal Year and Demographic"
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Crate a chart with the yearly trend line for the sum of encounter count by fiscal year and demographic. Add the sum of encounter count to the table.\n",
    "yearly_trend = encounters_aor_df.groupby(['Fiscal Year', 'Demographic'])['Encounter Count'].sum().unstack(fill_value=0)\n",
    "fig = px.line(yearly_trend.reset_index().melt(id_vars='Fiscal Year', var_name='Demographic', value_name='Encounter Count'),\n",
    "              x='Fiscal Year', y='Encounter Count', color='Demographic',\n",
    "              title='Yearly Trend of Total Encounters by Demographic',\n",
    "              labels={'Encounter Count': 'Total Encounters', 'Fiscal Year': 'Fiscal Year'})\n",
    "fig.update_traces(mode='lines+markers')\n",
    "fig.update_layout(yaxis_title='Total Encounters', xaxis_title='Fiscal Year FY21-FY24')\n",
    "fig.show()\n",
    "# Create a statistics table for the sum of encounter count by fiscal year and demographic. Add mean, median, standard deviation, variance, max, min to the table.\n",
    "yearly_trend_stats = yearly_trend.copy()\n",
    "yearly_trend_stats['Mean'] = yearly_trend.mean(axis=1)\n",
    "yearly_trend_stats['Median'] = yearly_trend.median(axis=1)\n",
    "yearly_trend_stats['Standard Deviation'] = yearly_trend.std(axis=1)\n",
    "yearly_trend_stats['Variance'] = yearly_trend.var(axis=1)\n",
    "yearly_trend_stats['Max'] = yearly_trend.max(axis=1)\n",
    "yearly_trend_stats['Min'] = yearly_trend.min(axis=1)\n",
    "import plotly.graph_objects as go\n",
    "# Prepare data for the table\n",
    "table = go.Figure(data=[go.Table(\n",
    "    header=dict(values=[\"Fiscal Year\", \"Demographic\", \"Sum\", \"Mean\", \"Median\", \"Standard Deviation\", \"Variance\", \"Max\", \"Min\"],\n",
    "                fill_color='paleturquoise',\n",
    "                align='left'),\n",
    "    cells=dict(values=[\n",
    "        yearly_trend_stats.index,  # Fiscal Year\n",
    "        yearly_trend_stats.columns,  # Demographic\n",
    "        yearly_trend_stats.values[:, 0],  # Sum\n",
    "        yearly_trend_stats['Mean'].round(2),  # Mean\n",
    "        yearly_trend_stats['Median'].round(2),  # Median\n",
    "        yearly_trend_stats['Standard Deviation'].round(2),  # Standard Deviation\n",
    "        yearly_trend_stats['Variance'].round(2),  # Variance\n",
    "        yearly_trend_stats['Max'],  # Max\n",
    "        yearly_trend_stats['Min']  # Min\n",
    "    ],\n",
    "    fill_color='lavender',\n",
    "    align='left'))\n",
    "])\n",
    "table.update_layout(title='Encounter Count Statistics by Fiscal Year and Demographic')\n",
    "table.show()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
