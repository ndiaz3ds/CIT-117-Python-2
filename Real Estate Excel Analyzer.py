import csv
#starts the import process for the RealEstate Data file
def getDataInput()->list:
    ldata = []
    with open('RealEstateData.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) #skips a file row
        for row in reader:
            ldata.append(row)
    return ldata

def getMedian(values: list[float])->float:
    n = len(values)
    sortedValues = sorted(values)
    if n % 2 == 0:
        mid = n//2
        return (sortedValues[mid-1] + sortedValues[mid]) /2
    else:
        return sortedValues[n//2]

def main():
    data=getDataInput()

    #process all that data and collect the accurate info
    fcity_totals: dict[str,float]={}
    fzip_totals: dict[str,float]={}
    fproperty_type_totals: dict[str,float]={}
    fproperty_prices: list[float]=[]
    for row in data:
        city = row[1]
        property_type = row[7]
        try:
            price = float(row[8])
        except ValueError:
            print(f"invalid price data, skipping row: {row[7]}")
            continue
        zip_code = row[2]

        #collect the property prices for the summary function
        fproperty_prices.append(price)

        #calculate all the summaries via city and property type
        if city not in fcity_totals:
            fcity_totals[city]=0
        fcity_totals[city] += price

        if zip_code not in fzip_totals:
            fzip_totals[zip_code]=0
        fzip_totals[zip_code] += price

        if property_type not in fproperty_type_totals:
            fproperty_type_totals[property_type]=0
        fproperty_type_totals[property_type] += price

        #output the summary functions for the property prices
    if fproperty_prices:
        fproperty_prices.sort()
        print(f"Minimum Property Price: ${fproperty_prices[0]:,.2f}")
        print(f"Maximum Property Price: ${fproperty_prices[-1]:,.2f}")
        print(f"Total Property Price: ${sum(fproperty_prices):,.2f}")
        print(f"Average Property Price: ${sum(fproperty_prices)/len(fproperty_prices):,.2f}")
        print(f"Median Property Price: ${getMedian(fproperty_prices):,.2f}")

    else:
        print("No data found")

    # list the summary by city
    print("\nSummary by City:")
    for city, total in fcity_totals.items():
        print(f"City: {city}, Total Price: ${total:,.2f}")

    #output the property type summary
    print("\nSummary by Property Type:")
    for ptype, total in fproperty_type_totals.items():
         print(f"Property Type: {ptype}, Total Price: ${total:,.2f}")

    #print the zip code
    print("\nSummary by Zip Code:")
    for zip_code, total in fzip_totals.items():
        print(f"Zip Code: {zip_code}, Total Price: ${total:,.2f}")

if __name__ == '__main__':
    main()



#Refection questions
#Name: Nicholas Diaz

#1. What did I like?
#  I enjoyed converting an excel file into data for python and learning new methods on how to handle the data

#2.What approach did I choose for the data and why?
#I chose to import it by the reader.csv as it was the easiest way possible and I made a data reader titled ldata.

#3.How many dictionaries did I use?
#I only used 3 dictionaries to get the job done.

#4. Two things I learned
#1.How to match up your rows based on what you want to output because sometimes I forget to check where my rows are lined up.
#2.More ways a dictionary can be useful in Python.
