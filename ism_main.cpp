#include "gen/ism__gen.hpp"
#include <iostream>

using namespace langcc;

int main(int argc, char** argv)
{
	langcc::global_init();
	langcc::set_log_level(1);

	if (argc < 2) {
		langcc::cout << "Error: No input file specified.\n";
		return 1;
	}

	std::ifstream sourcefile(argv[1]);
	std::stringstream buf;
	buf << sourcefile.rdbuf();

	auto L = lang::ism::init();
	auto Q = L->quote_env();
	langcc::unordered_map<langcc::string, langcc::Int> env;
	langcc::string text = buf.str();

	auto gen = langcc::make_rc<Gensym>();
	auto parse = L->parse_ext(
		langcc::vec_from_std_string(text),
		langcc::None<langcc::string>(),
		gen,
		nullptr
	);

	if (!parse->is_success()) {
		LG_ERR("\nParse error: {}\n", parse->err_.as_some());
	}
	else {
		langcc::pr_debug(cout, langcc::FmtFlags::default_(), parse->res_.as_some());
	}

}
