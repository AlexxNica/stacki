# $Id$
#
# @rocks@
# Copyright (c) 2000 - 2010 The Regents of the University of California
# All rights reserved. Rocks(r) v5.4 www.rocksclusters.org
# https://github.com/Teradata/stacki/blob/master/LICENSE-ROCKS.txt
# @rocks@
#
# $Log$
# Revision 1.5  2010/09/07 23:52:55  bruno
# star power for gb
#
# Revision 1.4  2010/05/11 22:28:16  bruno
# more tweaks
#
# Revision 1.3  2010/05/07 23:13:32  bruno
# clean up the help info for the firewall commands
#
# Revision 1.2  2010/05/04 22:04:15  bruno
# more firewall commands
#
# Revision 1.1  2010/04/30 22:07:16  bruno
# first pass at the firewall commands. we can do global and host level
# rules, that is, we can add, remove, open (calls add), close (also calls add),
# list and dump the global rules and the host-specific rules.
#
#

import stack.commands


class command(stack.commands.NetworkArgumentProcessor,
	stack.commands.list.command):
	pass


class Command(command):
	"""
	List the global firewall rules.
	<dummy />
	"""

	def run(self, params, args):
		self.beginOutput()

		self.db.execute("""select insubnet, outsubnet, service,
			protocol, chain, action, flags, comment, tabletype,
			name from global_firewall""")

		for i, o, s, p, c, a, f, cmt, tt, n in self.db.fetchall():
			network = self.getNetworkName(i)
			output_network = self.getNetworkName(o)

			self.addOutput('', (n, tt, s, p, c, a, network,
				output_network, f))

		self.endOutput(header=['', 'name', 'table', 'service',
			'protocol', 'chain', 'action', 'network',
			'output-network', 'flags'])

