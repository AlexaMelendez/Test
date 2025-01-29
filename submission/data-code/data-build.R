if (!require("pacman"))install.packages("pacman")
install.packages("languageserver", repos = "https://cran.r-project.org/")
pacman::p_load(tidyverse, ggplot2, dplyr, lubridate, stringr, readxl, data.table, gdata)

enroll.info=read_csv("data/input/CPSC_Enrollment_Info_2015_01.csv",
                         skip=1,
                         col_names = c("contractid","planid","fips", "state", "county", "enrollment"),
                         col_types = cols(
                           contractid = col_character(),
                           planid = col_double(),
                           ssa()
                           








