#include <cstdint>

#include "idiotic_json_variant.h"

IdioticJsonVariant::IdioticJsonVariant(bool value)  {

	variant.asBool = value;
	variantType = BOOL;

}

IdioticJsonVariant::IdioticJsonVariant(double value) {

	variant.asDouble = value;
	variantType = DOUBLE;

}

IdioticJsonVariant::IdioticJsonVariant(int64_t value) {

	variant.asInteger = value;
	variantType = INTEGER;

}

IdioticJsonVariant::IdioticJsonVariant(const char *value) {

	variant.asString = value;
	variantType = STRING;

}

