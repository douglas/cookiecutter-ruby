{% set class_name = cookiecutter.project_name.title().replace(' ', '') -%}
#!/usr/bin/env ruby
# frozen_string_literal: true

class {{ class_name }}
  class << self
    def run
      puts "Let's go!"
    end
  end
end

{{ class_name }}.run
