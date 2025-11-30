
popdata = {'CA': 39.5, 'TX': 30.0, 'FL': 22.2, 'NY': 19.8, 'PA': 13.0, 'IL': 12.8, 'OH': 11.8, 'GA': 10.9, 'NC': 10.7,
           'MI': 10.1}


def retrieve_pop(region_code, data_dict):
    if region_code in data_dict:
        return data_dict[region_code]
    else:
        return None


def main():
    valid_codes = []
    for code in popdata:
        valid_codes.append(code)

    while True:
        user_input = input(f"Please enter a country code: ")
        region_code = user_input.strip().upper()

        population = retrieve_pop(region_code, popdata)

        if population is not None:
            print(f"{region_code} population = {population}")
            break
        else:
            codes_string = ""
            for i in range(len(valid_codes)):
                if i == len(valid_codes) - 1:
                    codes_string += valid_codes[i]
                else:
                    codes_string += valid_codes[i] + ", "

            print(f"Error: '{region_code}' not recognized. Valid codes: {codes_string}")

            retry = input(f"Would you like to try again? (yes/no): ")
            retry_lower = retry.lower()

            if retry_lower == "yes" or retry_lower == "y":
                continue
            elif retry_lower == "no" or retry_lower == "n":
                print(f"Program terminated.")
                break


main()
