import smartsheet
import os
import dotenv

if __name__ == "__main__":
    def runScript():
        dotenv.load_dotenv()
        client = smartsheet.Smartsheet(access_token=os.getenv("TOKEN"))

        # The ID of the sheet you want to update
        sheet_id = os.getenv("SHEET_ID")  # Replace with your sheet ID
        
        # Retrieve the sheet to get column information
        sheet = client.Sheets.get_sheet(sheet_id)

        # Build a row with cell data
        new_row = smartsheet.models.Row()
        new_row.to_top = True  # Add the row to the top of the sheet (optional)

        # Populate the row with data for each column
        for column in sheet.columns:
            if column.title == "Primary Column":  # Replace with your column's name
                new_row.cells.append({
                    'column_id': column.id,
                    'value': 'Value 1'
                })
            elif column.title == "Column2":  # Replace with another column's name
                new_row.cells.append({
                    'column_id': column.id,
                    'value': 'Value 2'  # Example: Number
                })

        # Add the row to the sheet
        response = client.Sheets.add_rows(sheet_id, [new_row])

        # Print response
        print(f"Row added with ID: {response.result[0].id}")

runScript()
