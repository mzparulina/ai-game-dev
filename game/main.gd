
extends Control

@onready var decision_label: Label = $VBoxContainer/DecisionLabel
@onready var ask_button: Button = $VBoxContainer/AskButton
@onready var http_request: HTTPRequest = $HTTPRequest

const API_URL = "http://127.0.0.1:8000/npc/decide"


func _ready() -> void:
	ask_button.pressed.connect(ask_shopkeeper)
	http_request.request_completed.connect(_on_request_completed)


func ask_shopkeeper() -> void:
	decision_label.text = "Thinking..."
	ask_button.disabled = true

	var npc_state = {
		"energy": 80,
		"inventory": 10,
		"gold": 0
	}

	var headers = ["Content-Type: application/json"]

	var error = http_request.request(
		API_URL,
		headers,
		HTTPClient.METHOD_POST,
		JSON.stringify(npc_state)
	)

	if error != OK:
		decision_label.text = "Request failed."
		ask_button.disabled = false


func _on_request_completed(
	result: int,
	response_code: int,
	_headers: PackedStringArray,
	body: PackedByteArray
) -> void:
	ask_button.disabled = false

	if result != HTTPRequest.RESULT_SUCCESS:
		decision_label.text = "Connection error: " + str(result)
		return

	if response_code != 200:
		decision_label.text = "API error: " + str(response_code)
		return

	var data = JSON.parse_string(body.get_string_from_utf8())

	if typeof(data) != TYPE_DICTIONARY:
		decision_label.text = "Invalid response."
		return

	decision_label.text = str(data.get("decision", "No decision"))
