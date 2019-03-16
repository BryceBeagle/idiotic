#pragma once

#include <cstdint>
#include <ArduinoJson.h>


class IdioticJsonVariant {

	public:

		IdioticJsonVariant(bool value);

		IdioticJsonVariant(double value);

		IdioticJsonVariant(std::int64_t value);

		IdioticJsonVariant(const char *value);

		IdioticJsonVariant(JsonObject value);

		typedef union {
			bool asBool {};
			double asDouble;
			int64_t asInteger;
			const char *asString;

			// No JsonObjects because we're dumb and don't know how

		} Variant;

		Variant variant;

		enum VariantType {
			BOOL, DOUBLE, INTEGER, STRING, UNDEFINED
		};

		VariantType variantType;

};
