#include <chrono>

class TimeCounter
{
	public:
		TimeCounter() = default; //Ctor
		~TimeCounter() = default; //Dtor

		void start()
		{
			begin = std::chrono::high_resolution_clock::now();
		}

		void stop()
		{
			end = std::chrono::high_resolution_clock::now();
		}

		//Get time in seconds precision
		double get_duration_sec()
		{
			return std::chrono::duration<double>(end - begin).count();
		}

		//Get time in milliseconds precision
		double get_duration_msec()
		{
			return std::chrono::duration<double, std::milli>(end - begin).count();
		}

	private:
		std::chrono::system_clock::time_point begin;
		std::chrono::system_clock::time_point end;
};
