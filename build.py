from fs.osfs import OSFS
from fs.errors import ResourceInvalidError


# def create_title(title, summary)
	# title = '''
	#	<!-- <h2>%s</h2>
	#	            <p>%s</p> -->
	#''' % (tile, summary)

	# return title

# def create_substandard_title(standard, sub_standard):
	# title = '''
	# <p>
	# 	<i class="fa fa-file-o"></i>
	# 	<span style='margin-left: 25px'>
	# 		<a href="http://register.geostandaarden.nl/%s/%s">%s</a>
	# 	</span>
	# </p>
	#''' % (sub_standard, standard, sub_standard.capitalize())

	# return title

# def create_substandard_description(description):
	# summary = '''
	# <p>
	# 	<span style='margin-left:37px; width: 100%'>%s</span>
	# </p>
	# ''' % summary

	# return summary


# def build_web_page(standard, sub_standards, descriptions_path):
	# open standard configuration file that contains descriptions for each sub standard
	# descriptions = loadJSON(descriptions_path)

	# load standard HTML template

	# construct title
	# create_title(descriptions['title'])
	# append to #title

	# fetch #container from template

	# iterate over all sub_standards
		# for each type of sub_standard i.e. informatiemodel, gmlapplicatieschema, regels, etc.
			# create HTML snippet
				# title = create_substandard_title(standard, sub_standard)
				# append to #conainter
				# description = create_substandard_description(descriptions['sub-standards']['sub_standard'])
				# append to #container
	
	# return HTML page

# def create_overview_entry(standard, description):
	# overview = '''
	# 	<p>
	#		<i class="fa fa-file"></i>
	#		<span style='margin-left: 25px'>
	#			<a href="http://register.geostandaarden.nl/%s/">%s</a>
	#		</span>
	#	</p>
	# 	<p><span style='margin-left:37px; width: 100%'>%s</span></p>
 	#''' % (standard, standard.allCaps(), description)

 	# return overview

# def create_overview_page(standards):
	# open overview page template

	# fetch #leftcolumn element

	# iterate over standaards
		# if standard has informatiemodel substandard
			# description = fetch description from standard conf. file in repos/standard/conf.json
			# overview = create_overview_entry()
			# add to #leftcolumng element

	# save overview page to ./web/index.html

source = 'repos'
source_fs = OSFS(source)

destination = 'register/'

root = OSFS('./') # 'c:\Users\<login name>' on Windows
root.removedir(destination, force=True)
root.makedir(destination)

# iterate over the contents of source dir
standards = source_fs.listdir(dirs_only=True)
for standard in standards:
	print standard
	standard_fs = source_fs.opendir(standard)

	sub_standards = standard_fs.listdir(dirs_only=True)

	# iterate over dirs in each standard dir
	for sub_standard in sub_standards:
		# skip git dir
		if ".git" not in sub_standard:
			# check whether sub_standard folder exists in root
			if root.exists(destination + sub_standard) == False:
				root.makedir(destination + sub_standard)
				
			root.copydir('%s/%s/%s' % (source, standard, sub_standard),  '%s/%s/%s' % (destination, sub_standard, standard))

	# build_web_page(standard, sub_standards, source + '/' + standard + '/descriptions.json')
	# save HTML page to root/web/standard/index.html

# create_overview_page(standards)