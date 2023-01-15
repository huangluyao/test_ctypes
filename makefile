TARGET = test_ctypes.so 
SOURCES = *.cpp
$(TARGET):$(SOURCES)
	g++ -fPIC -shared -o $@ $<
	mkdir libs
	mv $@ libs

clean:
	rm -rf libs
rebuild:clean $(TARGET)