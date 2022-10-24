
gen/ism__gen.hpp: ism.lang
	langcc -h $< $@

clean:
	rm -rf build gen

.PHONY: clean
