#!/usr/bin/env python3

with open('gen/ism__gen.hpp', 'r') as fp:
	text = fp.read()

searchfor = """
    flags.sub_lo().advance_lines(1, os);
    os << "id: ";
    langcc::pr_debug(os, flags.sub_lo(), x->id_);
    os << ",";
    flags.sub_lo().advance_lines(1, os);
    os << "bounds: ";
    langcc::pr_debug(os, flags.sub_lo(), x->bounds_);
    os << ",";
    flags.sub_lo().advance_lines(1, os);
    os << "is_top: ";
    langcc::pr_debug(os, flags.sub_lo(), x->is_top_);
    os << ",";
    flags.sub_lo().advance_lines(1, os);
    os << "sym: ";
    langcc::pr_debug(os, flags.sub_lo(), x->sym_);
    os << ",";
    flags.sub_lo().advance_lines(1, os);
    os << "attr: ";
    langcc::pr_debug(os, flags.sub_lo(), x->attr_);
    os << ",";
    flags.sub_lo().advance_lines(1, os);
    os << "first_k: ";
    langcc::pr_debug(os, flags.sub_lo(), x->first_k_);
    os << ",";
"""

while (searchfor in text):
	text = text.replace(searchfor, '')

with open('gen/ism__gen.hpp', 'w') as fp:
	fp.write(text)
