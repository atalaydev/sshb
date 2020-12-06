PYTHON = python3

.PHONY: init test run

init:
	${PYTHON} -m pip install -r requirements.txt

test:
	@echo "Test cases are not implemented yet. Please checkout main branch of the project."

run:
	sshb
