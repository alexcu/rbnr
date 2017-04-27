bibnumber:
	@echo "Installing dependencies..."
	brew tap homebrew/science
	brew install opencv
	brew install tesseract
	brew install boost
	@echo "Cloning bibnumber..."
	git clone https://github.com/gheinrich/bibnumber.git bin/bibnumber
	@echo "Building bibnumber..."
	CPLUS_INCLUDE_PATH=/usr/local/include LIBRARY_PATH=/usr/local/lib make -C bin/bibnumber/bibnumber/Debug
