function create_Filter() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet1 = ss.getSheetByName("Filter_Sheet");

  var range = sheet1.getRange("A:X");

  //Add filter

  var filter = range.createFilter();

var Filter_Criteria1 = SpreadsheetApp.newFilterCriteria().whenTextEqualTo(["SEATTLE, USA"]);
var Filter_Criteria2 = SpreadsheetApp.newFilterCriteria().whenTextEqualTo(["TAMIL"]);


var add_filter1 = filter.setColumnFilterCriteria(18,Filter_Criteria1);
var add_filter2 = filter.setColumnFilterCriteria(15,Filter_Criteria2);

var range1 = sheet1.getDataRange();
var new_sheet =ss.insertSheet();
new_sheet.setName ("A Matches");
range1.copyTo(new_sheet.getRange(1,1));

filter.remove();

  
}
