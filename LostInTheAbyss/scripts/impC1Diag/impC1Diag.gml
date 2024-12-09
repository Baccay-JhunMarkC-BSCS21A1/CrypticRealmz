// Load JSON data from the file
var file_path = working_directory + "Chapter1.json";

if (file_exists(file_path)) {
    var file = file_text_open_read(file_path);
    var json_string = "";

    // Read the JSON file line by line
    while (!file_text_eof(file)) {
        json_string += file_text_readln(file);
    }
    file_text_close(file);

    // Parse the JSON into a map
    global.ch1_dialogue = json_parse(json_string);
} else {
	
}
