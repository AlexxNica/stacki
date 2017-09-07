# @SI_Copyright@
# Copyright (c) 2006 - 2017 StackIQ Inc.
# All rights reserved. stacki(r) v4.0 stacki.com
# https://github.com/Teradata/stacki/blob/master/LICENSE.txt
# @SI_Copyright@
#
# @Copyright@
# Copyright (c) 2000 - 2010 The Regents of the University of California
# All rights reserved. Rocks(r) v5.4 www.rocksclusters.org
# https://github.com/Teradata/stacki/blob/master/LICENSE-ROCKS.txt
# @Copyright@

import stack.commands

class Command(stack.commands.report.command):
	"""
	Output the version of Stacki.

	<example cmd='report version'>
	Output the current Stacki version.
	</example>
	"""

	def run(self, params, args):
		self.beginOutput()
		self.addOutput('', stack.version)
		self.endOutput()
